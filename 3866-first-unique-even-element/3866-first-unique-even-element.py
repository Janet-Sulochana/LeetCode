class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        e=0
        for i in nums:
            if i%2==0 and nums.count(i)==1:
                e=i
                return e
        return -1