class Solution:
    def secondHighest(self, s: str) -> int:
        res=[]
        for i in s:
            if i.isdigit():
                res.append(int(i))
        r=set(res)
        r=list(r)
        r.sort()
        if len(r)>1:
            return r[-2]
        else:
            return -1