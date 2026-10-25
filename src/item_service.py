import json
import math
from pathlib import Path
from typing import Any, Dict, List, Optional


class ItemService:
    def __init__(self, embedding_model, items_file_path: Optional[str] = None):
        self.embedding_model = embedding_model
        possible_paths = [
            Path(items_file_path) if items_file_path else None,
            Path(__file__).resolve().parent / "items.json",
            Path(__file__).resolve().parents[1] / "items.json",
            Path.cwd() / "items.json",
            Path.cwd() / "src" / "items.json",
        ]
        self.items_path = next((p for p in possible_paths if p and p.exists()), None)
        self.items: List[Dict[str, Any]] = []
        self.items_by_id: Dict[str, Dict[str, Any]] = {}
        self.item_embeddings: Dict[str, List[float]] = {}
        self._initialize_items()

    def _initialize_items(self):
        if not self.items_path or not self.items_path.exists():
            raise FileNotFoundError(f"Could not find items.json in any expected location.")

        with open(self.items_path, "r", encoding="utf-8") as f:
            self.items = json.load(f)

        for item in self.items:
            self.items_by_id[item["id"]] = item

        # Pre-embed all items using pairing text + description for semantic affinity
        texts_to_embed = []
        item_id_list = []
        for item in self.items:
            text = self._build_semantic_text(item)
            texts_to_embed.append(text)
            item_id_list.append(item["id"])

        embeddings = self.embedding_model.embed_batch(texts_to_embed)
        for item_id, embedding in zip(item_id_list, embeddings):
            self.item_embeddings[item_id] = embedding

        print(f"[ItemService] Initialized {len(self.items)} items with vector embeddings.")

    def _build_semantic_text(self, item: Dict[str, Any]) -> str:
        # Combining title, category, description and pairing text produces ideal semantic vectors
        name = item.get("name", "")
        category = item.get("category", "")
        description = item.get("description", "")
        pairing = item.get("pairing_text", "")
        return f"{name} ({category}): {description} Frequently paired with: {pairing}"

    def get_all_items(self) -> List[Dict[str, Any]]:
        return self.items

    def get_item(self, item_id: str) -> Optional[Dict[str, Any]]:
        if not item_id:
            return None
        # Exact match
        if item_id in self.items_by_id:
            return self.items_by_id[item_id]

        clean = item_id.lower().strip()
        clean_norm = clean.replace("-", "_")
        clean_no_prefix = clean_norm.removeprefix("item_")

        # 1. Check ID variations
        for it in self.items:
            it_id = it["id"].lower()
            it_norm = it_id.replace("-", "_")
            it_no_prefix = it_norm.removeprefix("item_")
            if clean_norm == it_norm or clean_no_prefix == it_no_prefix:
                return it

        # 2. Check title exact/substring match
        for it in self.items:
            name_lower = it["name"].lower()
            if clean in name_lower or all(w in name_lower for w in clean.split()):
                return it

        # 3. Check description / category match
        for it in self.items:
            if clean in it.get("category", "").lower() or clean in it.get("description", "").lower():
                return it

        return None

    def recommend_for_item(self, item_id: str, limit: int = 4) -> List[Dict[str, Any]]:
        target_item = self.get_item(item_id)
        if not target_item:
            raise ValueError(f"Item not found: {item_id}")

        target_embedding = self.item_embeddings.get(target_item["id"])
        if not target_embedding:
            raise ValueError(f"Embedding missing for item: {item_id}")

        matches = []
        for other_item in self.items:
            if other_item["id"] == target_item["id"]:
                continue

            other_embedding = self.item_embeddings.get(other_item["id"])
            if not other_embedding:
                continue

            similarity = self.cosine_similarity(target_embedding, other_embedding)

            match_data = dict(other_item)
            match_data["similarity"] = round(similarity, 4)
            match_data["similarity_percent"] = round(similarity * 100, 1)
            match_data["recommendation_reason"] = self._generate_reason(target_item, other_item, similarity)
            matches.append(match_data)

        matches.sort(key=lambda x: x["similarity"], reverse=True)
        return matches[:limit]

    def recommend_for_cart(self, cart_item_ids: List[str], limit: int = 4) -> List[Dict[str, Any]]:
        if not cart_item_ids:
            return self.items[:limit]

        # Resolve items to canonical IDs
        resolved_items = [self.get_item(cid) for cid in cart_item_ids]
        valid_items = [it for it in resolved_items if it and it["id"] in self.item_embeddings]
        cart_canonical_ids = {it["id"] for it in valid_items}
        valid_embeddings = [self.item_embeddings[it["id"]] for it in valid_items]

        if not valid_embeddings:
            return [it for it in self.items if it["id"] not in cart_canonical_ids][:limit]

        # Calculate basket centroid embedding (average vector)
        dim = len(valid_embeddings[0])
        centroid = [0.0] * dim
        for emb in valid_embeddings:
            for i in range(dim):
                centroid[i] += emb[i]
        centroid = [val / len(valid_embeddings) for val in centroid]

        matches = []
        for other_item in self.items:
            if other_item["id"] in cart_canonical_ids:
                continue

            other_embedding = self.item_embeddings.get(other_item["id"])
            if not other_embedding:
                continue

            similarity = self.cosine_similarity(centroid, other_embedding)

            match_data = dict(other_item)
            match_data["similarity"] = round(similarity, 4)
            match_data["similarity_percent"] = round(similarity * 100, 1)

            # Determine best pairing reason against individual items in cart
            best_reason = "Frequently bought with items in your cart"
            for cart_it in valid_items:
                reason = self._generate_reason(cart_it, other_item, similarity)
                if reason not in ("Highly Recommended Complementary Item", "Popular Companion Product"):
                    best_reason = reason
                    break
            match_data["recommendation_reason"] = best_reason
            matches.append(match_data)

        matches.sort(key=lambda x: x["similarity"], reverse=True)
        return matches[:limit]

    def search(self, query: str, limit: int = 6) -> List[Dict[str, Any]]:
        query_embedding = None
        try:
            query_embedding = self.embedding_model.embed(query)
        except Exception as e:
            print(f"[ItemService] Vector search fallback to keyword matching: {e}")

        if query_embedding:
            matches = []
            for item in self.items:
                item_embedding = self.item_embeddings.get(item["id"])
                if not item_embedding:
                    continue
                similarity = self.cosine_similarity(query_embedding, item_embedding)

                match_data = dict(item)
                match_data["similarity"] = round(similarity, 4)
                match_data["similarity_percent"] = round(similarity * 100, 1)
                matches.append(match_data)

            matches.sort(key=lambda x: x["similarity"], reverse=True)
            return matches[:limit]

        # Resilient keyword search fallback if embedding cannot be obtained
        q_tokens = [w.lower() for w in query.strip().split() if len(w) > 1]
        matches = []
        for item in self.items:
            score = 0.0
            name_lower = item["name"].lower()
            desc_lower = item["description"].lower()
            cat_lower = item["category"].lower()
            pair_lower = item.get("pairing_text", "").lower()

            for token in q_tokens:
                if token in name_lower:
                    score += 0.5
                if token in cat_lower:
                    score += 0.3
                if token in desc_lower or token in pair_lower:
                    score += 0.2

            if score > 0:
                match_data = dict(item)
                match_data["similarity"] = round(min(0.99, score), 4)
                match_data["similarity_percent"] = round(min(99.0, score * 100), 1)
                matches.append(match_data)

        matches.sort(key=lambda x: x["similarity"], reverse=True)
        return matches[:limit] if matches else self.items[:limit]


    def cosine_similarity(self, a: List[float], b: List[float]) -> float:
        dot_product = 0.0
        norm_a = 0.0
        norm_b = 0.0
        for i in range(len(a)):
            dot_product += a[i] * b[i]
            norm_a += a[i] * a[i]
            norm_b += b[i] * b[i]

        if norm_a == 0 or norm_b == 0:
            return 0.0
        return dot_product / (math.sqrt(norm_a) * math.sqrt(norm_b))

    def _generate_reason(
        self, target: Dict[str, Any], candidate: Dict[str, Any], similarity: float
    ) -> str:
        t_name = target["name"].lower()
        c_name = candidate["name"].lower()

        # Chai & Tea Pairings
        if ("tea" in t_name or "chai" in t_name) and "milk" in c_name:
            return "Essential Chai Element — Brew hot, rich, and creamy kadak masala chai"
        if ("tea" in t_name or "chai" in t_name) and "parle-g" in c_name:
            return "Legendary Chai Companion — Iconic biscuit made for dunking in hot chai"
        if ("tea" in t_name or "chai" in t_name) and "rusk" in c_name:
            return "Crunchy Evening Nashta — Cardamom elaichi crispy toast for your tea break"
        if ("tea" in t_name or "chai" in t_name) and "bhujia" in c_name:
            return "Chatpata Tea-Time Namkeen — Spicy crispy snack alongside hot cutting chai"

        # Pav & Bread Pairings
        if ("pav" in t_name or "bread" in t_name) and "butter" in c_name:
            return "Mumbai Maska Pav Match — Generous melt-in-mouth Amul butter for warm pav"
        if ("pav" in t_name or "bread" in t_name) and "egg" in c_name:
            return "Street-Style Anda Pav — Spicy egg bhurji or masala omelette with soft pav"
        if ("pav" in t_name or "bread" in t_name) and "cheese" in c_name:
            return "Crispy Cheese Toast — Quick grilled cheese sandwich & toast"

        # Maggi Pairings
        if "maggi" in t_name and "cheese" in c_name:
            return "Cheesy Maggi Upgrade — Slices melt into hot 2-minute masala noodles"
        if "maggi" in t_name and "butter" in c_name:
            return "Rich Butter Maggi — Street-style dollop of melting golden butter"

        # Dal Chawal & Roti Pairings
        if "dal" in t_name and "rice" in c_name:
            return "Dal Chawal Comfort — Quintessential Indian soul food comfort pairing"
        if "rice" in t_name and "dal" in c_name:
            return "Dal Chawal Comfort — Quintessential Indian soul food comfort pairing"
        if ("dal" in t_name or "rice" in t_name) and "ghee" in c_name:
            return "Aromatic Tadka Finishing — Pure golden cow ghee poured over hot dal chawal"
        if ("dal" in t_name or "rice" in t_name) and "jeera" in c_name:
            return "Jeera Tadka Secret — Earthy cumin seeds sizzled for dal fry and jeera rice"
        if "atta" in t_name and "ghee" in c_name:
            return "Soft Phulka & Roti Touch — Brushed over freshly puffed piping hot rotis"
        if "atta" in t_name and "dal" in c_name:
            return "Wholesome Indian Thali — Fresh soft rotis served with protein-rich dal fry"

        # Paneer & Spices
        if "paneer" in t_name and ("garam masala" in c_name or "mirch" in c_name):
            return "Shahi Gravy Spice — Aromatic spice blend for rich restaurant-style paneer curry"
        if "paneer" in t_name and "butter" in c_name:
            return "Paneer Butter Masala — Essential creamy dairy butter for silky makhani gravy"

        # Idli / Dosa Batter
        if "batter" in t_name and ("dal" in c_name or "ghee" in c_name):
            return "Crispy Ghee Roast & Sambar — Golden crisp restaurant dosas & hot dal sambar"

        # Coffee & Milk
        if "coffee" in t_name and "milk" in c_name:
            return "Creamy Frothy Cuppa — Frothy hot beaten coffee or cold iced frappe"

        # Rooh Afza & Milk
        if "rooh afza" in t_name and "milk" in c_name:
            return "Royal Gulab Sharbat — Sweet refreshing rose milk drink"

        if similarity > 0.65:
            return "Highly Recommended Indian Grocery Companion"
        return "Popular Complementary Item"

