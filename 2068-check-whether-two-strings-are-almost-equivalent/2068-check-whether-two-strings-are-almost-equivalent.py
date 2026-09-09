class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        f=[0]*26
        for c in word1:
            f[ord(c)-ord('a')]+=1
        for c in word2:
            f[ord(c)-ord('a')]-=1
        return all(abs(diff)<=3 for diff in f)