class Solution:
    def modifyString(self, s: str) -> str:
        res=list(s)
        n=len(res)
        for i in range(n):
            if res[i]=='?':
                for ch in ('a','b','c'):
                    if i>0 and res[i-1]==ch:
                        continue
                    if i<len(res)-1 and res[i+1]==ch:
                        continue
                    res[i]=ch
                    break
        return "".join(res)