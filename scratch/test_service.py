import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.embedding_model import OpenAIEmbeddingModel
from src.item_service import ItemService

print("Initializing ItemService...")
model = OpenAIEmbeddingModel()
service = ItemService(embedding_model=model)

items = service.get_all_items()
print(f"Total items loaded: {len(items)}")

# Test single item recommendation
rec = service.recommend_for_item("item_tata_tea", limit=4)
print(f"\nRecommendations for item_tata_tea ({len(rec)} items):")
for r in rec:
    print(f" - {r['name']} ({r['similarity_percent']}% Match, Reason: {r['recommendation_reason']})")

# Test cart recommendation
cart_rec = service.recommend_for_cart(["item_toor_dal", "item_basmati_rice"], limit=4)
print(f"\nCart recommendations for [Toor Dal, Basmati Rice]:")
for r in cart_rec:
    print(f" - {r['name']} ({r['similarity_percent']}% Match, Reason: {r['recommendation_reason']})")

# Test semantic search
search_res = service.search("crunchy spicy snack for evening tea", limit=4)
print(f"\nSearch results for 'crunchy spicy snack for evening tea':")
for r in search_res:
    print(f" - {r['name']} ({r['similarity_percent']}% Match)")
