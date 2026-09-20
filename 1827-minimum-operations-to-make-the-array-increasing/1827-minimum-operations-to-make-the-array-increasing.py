class Solution:
    def minOperations(self, nums: List[int]) -> int:
        op=0
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                inc=nums[i-1]-nums[i]+1
                op+=inc
                nums[i]+=inc
        return op