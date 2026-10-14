class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        res=[]
        for i in range(num):
            digit=min(9,sum)
            res.append(str(digit))
            sum-=digit
        if sum>0:
            return ""
        return "".join(res)