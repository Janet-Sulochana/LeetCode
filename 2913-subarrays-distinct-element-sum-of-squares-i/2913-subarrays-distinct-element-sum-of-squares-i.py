class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        result=0
        for i in range(len(nums)):
            s=set()
            for j in range(i,len(nums)):
                s.add(nums[j])
                result+=len(s)**2
        return result