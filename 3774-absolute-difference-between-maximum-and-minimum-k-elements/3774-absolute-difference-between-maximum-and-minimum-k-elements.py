class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_s=sum(nums[-k:])
        min_s=sum(nums[:k])
        return abs(max_s-min_s)
