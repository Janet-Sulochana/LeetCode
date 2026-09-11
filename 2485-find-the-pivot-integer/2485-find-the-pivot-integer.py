class Solution:
    def pivotInteger(self, n: int) -> int:
        t_s=n*(n+1)//2
        p=int(math.sqrt(t_s))
        if p*p==t_s:
            return p
        return -1