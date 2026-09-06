class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        s=set(nums)
        t=0
        for i in s:
            n=nums.count(i)
            if n%k==0:
                t+=i*n
        return t if t else 0