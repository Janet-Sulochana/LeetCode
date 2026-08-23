class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        summ=0
        n=set(nums)
        for i in n:
            if nums.count(i)==1:
                summ+=i
        return summ