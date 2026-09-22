class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        t=sum(nums)
        if t<abs(target) or (t+target)%2!=0:
            return 0
        s=(t+target)//2
        dp=[0]*(s+1)
        dp[0]=1
        for num in nums:
            for i in range(s,num-1,-1):
                dp[i]+=dp[i-num]
        return dp[s]