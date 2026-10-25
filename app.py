"""
ASGI entry point for deployment platforms (Render, Railway, Vercel, etc.)
Enables running the server with:
  uvicorn app:app --host 0.0.0.0 --port $PORT
"""
import sys
from pathlib import Path

# Add root and src directories to Python path
root_dir = Path(__file__).resolve().parent
src_dir = root_dir / "src"

for directory in [str(root_dir), str(src_dir)]:
    if directory not in sys.path:
        sys.path.insert(0, directory)

from src.main import app  # noqa: F401
