from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

WORKSPACE_DIR = BASE_DIR / "workspace"
UPLOAD_DIR = BASE_DIR / "uploads"
VECTOR_DB_DIR = BASE_DIR / "vector_db"

for directory in [WORKSPACE_DIR, UPLOAD_DIR, VECTOR_DB_DIR]:
    directory.mkdir(parents=True, exist_ok=True)