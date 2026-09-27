class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        k=0
        nums.sort(reverse=True)
        for i in nums:
            if i and -i in nums:
                return i
        return -1