class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        s=str(n)
        t=str(x)
        return t in s and s[0]!=t