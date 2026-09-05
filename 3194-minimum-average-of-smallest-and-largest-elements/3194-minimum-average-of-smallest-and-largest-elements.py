class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        res=[]
        while nums:
            a=nums.pop()
            b=min(nums)
            nums.remove(b)
            av=(a+b)/2
            res.append(av)
        res.sort()
        return res[0]