class Solution:
    def checkDivisibility(self, n: int) -> bool:
        temp=n
        d_s=0
        d_p=1
        while temp>0:
            d=temp%10
            d_s+=d
            d_p*=d
            temp//=10
        return n%(d_s+d_p)==0