class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        res=[]
        nums.sort(reverse=True)
        while nums:
            a=nums.pop()
            b=nums.pop()
            res.append(b)
            res.append(a)
        return res

