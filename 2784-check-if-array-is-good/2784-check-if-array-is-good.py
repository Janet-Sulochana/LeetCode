class Solution:
    def isGood(self, nums: List[int]) -> bool:
        m=max(nums)
        nums.sort()
        for i in range(1,m):
            if nums.count(i)!=1:
                return False
        return nums.count(m)==2 and len(nums)==m+1