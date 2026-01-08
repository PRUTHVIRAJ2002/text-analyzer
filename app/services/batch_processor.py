from concurrent.futures import ThreadPoolExecutor
from ..utils.file_loader import load_text
from ..services.text_analyzer import TextAnalyzer

def process_file(file_path: str, analyses: list):
    text = load_text(file_path)
    result = {}

    if "word_frequency" in analyses:
        result["word_frequency"] = TextAnalyzer.word_frequency(text)

    if "sentence_start" in analyses:
        result["sentence_start"] = TextAnalyzer.sentence_start_words(text)

    if "sentence_stats" in analyses:
        result["sentence_stats"] = TextAnalyzer.sentence_length_stats(text)

    return result

def process_files_parallel(files: list, analyses: list):
    results = {}
    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(process_file, f, analyses): f for f in files}
        for future in futures:
            results[futures[future]] = future.result()
    return results
