class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        r=0
        for i in range(32):
            c=0
            for num in nums:
                if (num>>i)&1:
                    c+=1
            if c>=k:
                r|= (1<<i)
        return r