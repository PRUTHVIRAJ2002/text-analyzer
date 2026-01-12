import os
from fastapi import HTTPException

BASE_DIR = "data"

def load_text(file_path: str) -> str:
    full_path = os.path.join(BASE_DIR, file_path)

    if not os.path.exists(full_path):
        raise HTTPException(status_code=404, detail="File not found")

    with open(full_path, "r", encoding="utf-8") as f:
        return f.read()
