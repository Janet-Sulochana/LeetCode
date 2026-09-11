class Solution:
    def countEven(self, num: int) -> int:
        d_s=sum(int(d) for d in str(num))
        if d_s%2==0:
            return num//2
        else:
            return (num-1)//2