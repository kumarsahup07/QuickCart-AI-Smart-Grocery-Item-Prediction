import os
import sys
from pathlib import Path

# Fix Windows console encoding
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Add src and root to path
root_dir = Path(__file__).resolve().parent
src_dir = root_dir / "src"

for d in [str(root_dir), str(src_dir)]:
    if d not in sys.path:
        sys.path.insert(0, d)

# Import the FastAPI app instance from src/main.py
from src.main import app  # noqa: E402

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


