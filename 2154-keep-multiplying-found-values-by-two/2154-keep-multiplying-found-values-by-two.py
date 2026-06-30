class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums.sort()
        n=len(nums)
        for i in range(n):
            l=0
            r=n-1
            while(l<=r):
                mid=(l+r)//2
                if nums[mid]==original:
                    original=2*original
                elif nums[mid]<original:
                    l=mid+1
                else:
                    r=mid-1    
        return original