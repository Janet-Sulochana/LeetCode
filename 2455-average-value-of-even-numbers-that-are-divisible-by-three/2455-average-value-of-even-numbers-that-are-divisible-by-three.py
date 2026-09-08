class Solution:
    def averageValue(self, nums: List[int]) -> int:
        s=0
        c=0
        for i in nums:
            if i%2==0 and i%3==0:
                s+=i
                c+=1
        if c:
            return s//c
        return 0