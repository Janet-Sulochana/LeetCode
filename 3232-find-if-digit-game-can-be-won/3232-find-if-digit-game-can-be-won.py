class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        s=0
        d=0
        for num in nums:
            if num<10:
                s+=num
            else:
                d+=num
        return s!=d