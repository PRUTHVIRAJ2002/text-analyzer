import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# BASE_DIR = /app/app

PROJECT_ROOT = os.path.dirname(BASE_DIR)
# PROJECT_ROOT = /app

def load_text(file_path: str) -> str:
    full_path = os.path.join(PROJECT_ROOT, file_path)

    if not os.path.exists(full_path):
        raise FileNotFoundError(f"File not found: {full_path}")

    with open(full_path, "r", encoding="utf-8") as f:
        return f.read()
