from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        c=Counter(words[0])
        for word in words[1:]:
            c&=Counter(word)
        return list(c.elements())