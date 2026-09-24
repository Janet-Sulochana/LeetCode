class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            s=0
            n=nums[i]
            while n>0:
                d=n%10
                s+=d
                n//=10
            if i==s:
                return i
        return -1