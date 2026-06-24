class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        l=0
        for l in range(n):
            for r in range(l+1,n):
                if nums[l]>nums[r]:
                    temp=nums[r]
                    nums[r]=nums[l]
                    nums[l]=temp
            

        
        