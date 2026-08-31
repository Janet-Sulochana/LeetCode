from collections import Counter
from typing import List
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        target_counts = Counter(c.lower() for c in licensePlate if c.isalpha())

        best_word = None

        for word in words:
            word_counts = Counter(word)
        
            if all(word_counts[ch] >= count for ch, count in target_counts.items()):
                if best_word is None or len(word) < len(best_word):
                    best_word = word

        return best_word