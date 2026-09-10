class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        c=set(nums[0])
        for a in nums[1:]:
            c&=set(a)

        return sorted(list(c))