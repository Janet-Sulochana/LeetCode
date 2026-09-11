class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        s=[]
        n=len(nums)
        for i in range(2**n):
            u=[]
            for j in range(n):
                if i&(1<<j):
                    u.append(nums[j])
            s.append(u)
        return s