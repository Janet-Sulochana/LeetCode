class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s>9*n:
            return -1
        d=[]
        for i in range(n):
            t=min(9,s)
            d.append(str(t))
            s-=t
        return int("".join(d))