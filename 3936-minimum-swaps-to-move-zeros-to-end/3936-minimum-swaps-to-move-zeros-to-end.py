class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        k=nums.count(0)
        if k==0:
            return 0
        return sum(1 for x in nums[-k:] if x!=0)