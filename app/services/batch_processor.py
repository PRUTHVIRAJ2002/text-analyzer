from concurrent.futures import ThreadPoolExecutor
from ..utils.file_loader import load_text
from .text_analyzer import TextAnalyzer
from .bigquery_service import save_to_bigquery

def process_file(file_path: str, analyses: list):
    text = load_text(file_path)
    result = {}

    if "word_frequency" in analyses:
        wf = TextAnalyzer.word_frequency(text)
        result["word_frequency"] = wf
        for word, count in wf:
            save_to_bigquery(file_path, "word_frequency", word, count)

    if "sentence_start" in analyses:
        ss = TextAnalyzer.sentence_start_words(text)
        result["sentence_start"] = ss
        for word, count in ss:
            save_to_bigquery(file_path, "sentence_start", word, count)

    if "sentence_stats" in analyses:
        stats = TextAnalyzer.sentence_length_stats(text)
        result["sentence_stats"] = stats
        for k, v in stats.items():
            save_to_bigquery(file_path, "sentence_stats", k, v)

    return result

def process_files_parallel(files: list, analyses: list):
    results = {}
    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(process_file, f, analyses): f for f in files}
        for future in futures:
            results[futures[future]] = future.result()
    return results
