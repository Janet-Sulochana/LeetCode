class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        res=sorted(nums)
        if len(res)==1:
            return 0
        if res[-1]>=2*res[-2]:
            return nums.index(res[-1])
        return -1
