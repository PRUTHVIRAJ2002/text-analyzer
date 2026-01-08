import re
import statistics
from collections import Counter
from ..utils.stopwords import STOP_WORDS

class TextAnalyzer:

    @staticmethod
    def word_frequency(text: str):
        words = re.findall(r'\b[a-z]+\b', text.lower())
        filtered = [w for w in words if w not in STOP_WORDS]
        return Counter(filtered).most_common(20)

    @staticmethod
    def sentence_start_words(text: str):
        sentences = re.split(r'[.!?]', text)
        starts = []
        for s in sentences:
            words = re.findall(r'\b[a-z]+\b', s.lower())
            if words:
                starts.append(words[0])
        return Counter(starts).most_common(10)

    @staticmethod
    def sentence_length_stats(text: str):
        sentences = re.split(r'[.!?]', text)
        lengths = [len(re.findall(r'\b[a-z]+\b', s)) for s in sentences if s.strip()]
        return {
            "mean": statistics.mean(lengths),
            "median": statistics.median(lengths),
            "std_dev": statistics.stdev(lengths) if len(lengths) > 1 else 0
        }
