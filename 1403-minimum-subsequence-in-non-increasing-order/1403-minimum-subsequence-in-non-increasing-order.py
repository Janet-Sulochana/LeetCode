class Solution:
    def minSubsequence(self, nums: list[int]) -> list[int]:
        nums.sort(reverse=True)
        total_sum=sum(nums)
        sub_sum=0
        res=[]
        for num in nums:
            sub_sum+=num
            res.append(num)
            if sub_sum>total_sum-sub_sum:
                break
        return res