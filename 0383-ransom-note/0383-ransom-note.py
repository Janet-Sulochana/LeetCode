from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r=Counter(ransomNote)
        m=Counter(magazine)
        return all(r[c]<=m[c] for c in r)