import os
import sys
from pathlib import Path
from typing import List, Optional

# Fix Windows console encoding
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Add current directory to path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from embedding_model import OpenAIEmbeddingModel
from item_service import ItemService

# Load environment variables
load_dotenv()
load_dotenv(Path(__file__).resolve().parents[1] / ".env")

app = FastAPI(
    title="Smart Shopping Cart - Item Prediction & Recommendation Engine",
    description="Vector Embedding-based Item Recommendation & Basket Prediction Engine",
    version="1.0.0",
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

embedding_model = OpenAIEmbeddingModel()
item_service = ItemService(embedding_model)

possible_frontend_dirs = [
    Path(__file__).resolve().parents[1] / "frontend",
    Path(__file__).resolve().parent / "frontend",
    Path.cwd() / "frontend",
]
frontend_dir = next((d for d in possible_frontend_dirs if d.exists()), None)


class CartRequest(BaseModel):
    item_ids: List[str]
    limit: Optional[int] = 4


@app.get("/api/items")
def get_items():
    """Retrieve all catalog items."""
    return item_service.get_all_items()


@app.get("/api/items/{item_id}")
def get_item(item_id: str):
    """Retrieve single item by ID or name."""
    item = item_service.get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"Item '{item_id}' not found.")
    return item


@app.get("/api/recommend/{item_id}")
def recommend_for_item(
    item_id: str,
    limit: int = Query(4, ge=1, le=10, description="Number of recommendations"),
):
    """Predict and recommend complementary items (e.g. Bread -> Butter, Jam, Milk)."""
    try:
        return item_service.recommend_for_item(item_id, limit=limit)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.post("/api/recommend/cart")
def recommend_for_cart(payload: CartRequest):
    """Predict complementary items for all items currently in cart (basket completion)."""
    return item_service.recommend_for_cart(payload.item_ids, limit=payload.limit or 4)


@app.get("/api/search")
def search_items(
    q: str = Query(..., description="Semantic search query (e.g. 'breakfast spreads', 'movie snacks')"),
    limit: int = Query(6, ge=1, le=12),
):
    """Semantic vector search across item catalog."""
    return item_service.search(q, limit=limit)


# Mount frontend static files at root
if frontend_dir and frontend_dir.exists():
    app.mount("/", StaticFiles(directory=str(frontend_dir), html=True), name="frontend")


if __name__ == "__main__":
    import uvicorn

    port = int(os.getenv("PORT", 8000))
    host = os.getenv("HOST", "0.0.0.0")

    print("=" * 65)
    print(f"[QuickCart AI] Starting FastAPI Server on http://{host}:{port}")
    print(f"[Web UI] Open http://localhost:{port} in your browser to view the shop!")
    print(f"[Docs] Open http://localhost:{port}/docs for Swagger API documentation")
    print("=" * 65)

    uvicorn.run(app, host=host, port=port)



