class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        r=""
        for i in words:
            r+=i[0]
        return r==s