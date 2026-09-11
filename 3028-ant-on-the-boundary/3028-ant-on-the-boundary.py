class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        p=0
        bc=0
        for num in nums:
            p+=num
            if p==0:
                bc+=1
        return bc