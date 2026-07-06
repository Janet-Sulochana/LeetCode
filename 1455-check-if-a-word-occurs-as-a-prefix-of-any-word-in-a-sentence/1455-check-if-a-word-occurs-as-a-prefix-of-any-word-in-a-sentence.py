class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        l=sentence.split()
        n=len(l)
        for i in range(n):
            if l[i].startswith(searchWord):
                return i+1
        return -1