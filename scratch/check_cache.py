import json
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from src.embedding_model import OpenAIEmbeddingModel

m = OpenAIEmbeddingModel()
print(f"Cached entries in model: {len(m.cache)}")

items = json.loads(Path("items.json").read_text(encoding="utf-8"))
print(f"Total items in items.json: {len(items)}")

def build_text(it):
    name = it.get("name", "")
    category = it.get("category", "")
    description = it.get("description", "")
    pairing = it.get("pairing_text", "")
    return f"{name} ({category}): {description} Frequently paired with: {pairing}".strip()

missing = [build_text(it) for it in items if build_text(it) not in m.cache]
print(f"Missing embeddings count: {len(missing)}")
