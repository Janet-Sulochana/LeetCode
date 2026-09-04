class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        nums.sort()
        a=nums[-1]
        b=nums[-2]
        c=nums[0]
        return a+b-c