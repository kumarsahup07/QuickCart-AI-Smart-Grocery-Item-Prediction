import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.embedding_model import OpenAIEmbeddingModel

CACHE_SRC = ROOT / "src" / "embeddings_cache.json"
CACHE_ROOT = ROOT / "embeddings_cache.json"

print(f"Loading embedding model with primary cache at: {CACHE_SRC}")
model = OpenAIEmbeddingModel(cache_file=str(CACHE_SRC))

items_path = ROOT / "items.json"
items = json.loads(items_path.read_text(encoding="utf-8"))
print(f"Total items in catalog: {len(items)}")

def build_text(it):
    name = it.get("name", "")
    category = it.get("category", "")
    description = it.get("description", "")
    pairing = it.get("pairing_text", "")
    return f"{name} ({category}): {description} Frequently paired with: {pairing}".strip()

texts = [build_text(it) for it in items]
missing = [t for t in texts if t not in model.cache]
print(f"Need to embed {len(missing)} items in batches of 100...")

if missing:
    start_time = time.time()
    embeddings = model.embed_batch(texts)
    elapsed = time.time() - start_time
    print(f"Embedding completed in {elapsed:.2f}s! Total cache entries now: {len(model.cache)}")
else:
    print("All items are already cached!")

# Sync to both root and src
CACHE_SRC.write_text(json.dumps(model.cache, indent=2), encoding="utf-8")
CACHE_ROOT.write_text(json.dumps(model.cache, indent=2), encoding="utf-8")
print(f"Saved complete embeddings cache ({len(model.cache)} items) to {CACHE_SRC} and {CACHE_ROOT}")
