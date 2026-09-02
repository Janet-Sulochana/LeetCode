class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        c=0
        n=len(nums)
        for i in range(1,n):
            if nums[i]<=nums[i-1]:
                c+=1
                if c>1:
                    return False
                if i>1 and nums[i]<=nums[i-2]:
                    nums[i]=nums[i-1]
        return True