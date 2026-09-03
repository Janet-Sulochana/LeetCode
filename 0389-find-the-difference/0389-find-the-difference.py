class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res=0
        for i in s:
            res=res^ord(i)
        for i in t:
            res=res^ord(i)
        return chr(res)