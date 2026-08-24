class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        total=ans=0
        for x in nums:
            total+=x
            ans=min(ans,total)
        return 1-ans