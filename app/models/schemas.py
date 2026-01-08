from pydantic import BaseModel
from typing import List

class AnalyzeRequest(BaseModel):
    file_path: str
    analyses: List[str]

class BatchAnalyzeRequest(BaseModel):
    files: List[str]
    analyses: List[str]
