class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n=len(nums)
        l=0
        r=n-1
        while l<r:
            if nums[l]%2 >nums[r]%2:
                temp=nums[l]
                nums[l]=nums[r]
                nums[r]=temp
            if nums[l]%2==0:
                l+=1
            if nums[r]%2!=0:
                r-=1
        return nums