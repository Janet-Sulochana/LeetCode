class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        n=len(nums)
        mins=n+1
        summ=0
        for r in range(n):
            summ+=nums[r]
            while summ>=target:
                mins=min(mins,r-l+1)
                summ-=nums[l]
                l+=1
        return mins if mins!=n+1 else 0