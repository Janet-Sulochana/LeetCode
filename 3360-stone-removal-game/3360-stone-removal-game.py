class Solution:
    def canAliceWin(self, n: int) -> bool:
        k=10
        while n>=k:
            n-=k
            k-=1
        return k%2==1