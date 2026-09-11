class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        n=len(nums)
        dc=0
        di=-1
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                dc+=1
                di=i
        if dc==0:
            return 0
        if dc>1:
            return -1
        if nums[-1]<nums[0]:
            return n-1-di
        else:
            return -1