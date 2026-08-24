class Solution:
    def arraySign(self, nums: List[int]) -> int:
        neg=sum(x<0 for x in nums)
        if 0 in nums:
            return 0
        return -1 if neg %2 else 1