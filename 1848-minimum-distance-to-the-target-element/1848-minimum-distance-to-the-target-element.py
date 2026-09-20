class Solution:
    def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
        ans=float('inf')
        for i, num in enumerate(nums):
            if num==target:
                ans=min(ans,abs(i-start))
        return ans