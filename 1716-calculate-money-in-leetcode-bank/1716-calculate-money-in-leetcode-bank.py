class Solution:
    def totalMoney(self, n: int) -> int:
        t=0
        for i in range(n):
            t+=(i//7)+(i%7)+1
        return t