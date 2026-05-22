class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l,h=0,len(nums)-1
        while(l<h):
            mid=(h+l)//2
            if(nums[mid]<nums[mid+1]):
                l=mid+1
            else:
                h=mid
        return l 