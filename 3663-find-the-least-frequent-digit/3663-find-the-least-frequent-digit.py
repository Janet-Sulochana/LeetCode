class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        res=[]
        f=float('inf')
        s=str(n)
        r=set(s)
        for i in r:
            c=s.count(i)
            f=min(f,c)
        for i in r:
            c=s.count(i)
            if c==f:
                res.append(int(i))
        return min(res)
