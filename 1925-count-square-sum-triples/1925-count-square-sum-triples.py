class Solution:
    def countTriples(self, n: int) -> int:
        c=0
        s=set(i*i for i in range(1,n+1))
        for a in range(1,n):
            for b in range(1,n):
                if a*a+b*b in s:
                    c+=1
        return c