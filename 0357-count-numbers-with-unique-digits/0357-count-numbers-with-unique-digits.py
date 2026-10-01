class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n==0:
            return 1
        ans=10
        avail=9
        uniq=9
        for i in range(2,n+1):
            uniq=uniq*avail
            ans+=uniq
            avail-=1
        return ans