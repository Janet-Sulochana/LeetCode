class Solution:
    def thousandSeparator(self, n: int) -> str:
        s=str(n)
        res=[]
        for i,ch in enumerate(reversed(s)):
            if i>0 and i%3==0:
                res.append(".")
            res.append(ch)
        return "".join(reversed(res))