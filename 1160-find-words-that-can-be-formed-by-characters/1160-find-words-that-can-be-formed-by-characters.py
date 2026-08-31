class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total_length=0
        for word in words:
            if all(chars.count(c)>=word.count(c) for c in set(word)):
                total_length+=len(word)
        return total_length