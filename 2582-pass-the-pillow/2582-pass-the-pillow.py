class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        f=time//(n-1)
        r=time%(n-1)
        if f%2==0:
            return 1+r
        else:
            return n-r