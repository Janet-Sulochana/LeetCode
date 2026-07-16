class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        w_sum=0
        n=len(nums)
        for i in range(k):
            w_sum+=nums[i]
        max_sum=w_sum
        for i in range(k,n):
            w_sum+=nums[i]
            w_sum-=nums[i-k]
            max_sum=max(max_sum,w_sum)
        return max_sum/k