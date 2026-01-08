from fastapi import APIRouter
from ..models.schemas import AnalyzeRequest, BatchAnalyzeRequest
from ..utils.file_loader import load_text
from ..services.text_analyzer import TextAnalyzer
from ..services.batch_processor import process_files_parallel

router = APIRouter()

@router.post("/analyze")
def analyze(req: AnalyzeRequest):
    text = load_text(req.file_path)
    result = {}

    if "word_frequency" in req.analyses:
        result["word_frequency"] = TextAnalyzer.word_frequency(text)

    if "sentence_start" in req.analyses:
        result["sentence_start"] = TextAnalyzer.sentence_start_words(text)

    if "sentence_stats" in req.analyses:
        result["sentence_stats"] = TextAnalyzer.sentence_length_stats(text)

    return result

@router.post("/analyze-batch")
def analyze_batch(req: BatchAnalyzeRequest):
    return process_files_parallel(req.files, req.analyses)
