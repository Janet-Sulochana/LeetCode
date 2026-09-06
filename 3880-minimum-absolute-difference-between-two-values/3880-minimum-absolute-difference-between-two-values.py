class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        m=float('inf')
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]==1 and nums[j]==2:
                    mi=abs(i-j)
                    m=min(m,mi)
        
        return m if m!=float('inf') else -1