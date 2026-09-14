class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        or_s=0
        for num in nums:
            or_s|=num
        return or_s<<(len(nums)-1)