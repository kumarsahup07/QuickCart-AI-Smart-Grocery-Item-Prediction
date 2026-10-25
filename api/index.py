import sys
from pathlib import Path

# Add project root and src directory to sys.path
root_dir = Path(__file__).resolve().parent.parent
src_dir = root_dir / "src"

for d in [str(root_dir), str(src_dir)]:
    if d not in sys.path:
        sys.path.insert(0, d)

from main import app
