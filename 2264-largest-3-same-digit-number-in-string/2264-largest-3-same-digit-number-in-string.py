class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for i in range(9,-1,-1):
            c=str(i)*3
            if c in num:
                return c
        return ""