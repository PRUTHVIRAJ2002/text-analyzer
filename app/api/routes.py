from fastapi import APIRouter
from ..models.schemas import AnalyzeRequest, BatchAnalyzeRequest
from ..services.batch_processor import process_file, process_files_parallel

router = APIRouter()

@router.post("/analyze")
def analyze(req: AnalyzeRequest):
    return process_file(req.file_path, req.analyses)

@router.post("/analyze-batch")
def analyze_batch(req: BatchAnalyzeRequest):
    return process_files_parallel(req.files, req.analyses)
