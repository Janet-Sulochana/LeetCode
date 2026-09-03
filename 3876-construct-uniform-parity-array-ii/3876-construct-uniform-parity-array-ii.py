class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        return not (min(nums1) ^ reduce(or_, nums1)) & 1