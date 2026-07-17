class Solution:
    def findLHS(self, nums: List[int]) -> int:
        l=0
        max_len=0
        nums.sort()
        n=len(nums)
        for r in range(n):
            while nums[r]-nums[l]>1:
                l+=1
            if nums[r]-nums[l]==1:
                max_len=max(max_len,r-l+1)
        return max_len