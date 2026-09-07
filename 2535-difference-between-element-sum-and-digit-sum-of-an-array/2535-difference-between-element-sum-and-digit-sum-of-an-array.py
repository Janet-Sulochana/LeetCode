class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        es=0
        ds=0
        r=""
        for i in nums:
            r+=str(i)
            es+=i
        for i in r:
            ds+=int(i)
        return abs(es-ds)