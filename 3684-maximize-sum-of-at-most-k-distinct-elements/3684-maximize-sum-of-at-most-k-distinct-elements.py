class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        s=set(nums)
        s=list(s)
        s.sort(reverse=True)
        if len(s)>k:
            return s[:k]
        return s