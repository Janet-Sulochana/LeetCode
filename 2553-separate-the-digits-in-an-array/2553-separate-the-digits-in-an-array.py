class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        s=""
        for i in nums:
            s+=str(i)
        r=[]
        for i in s:
            r.append(int(i))
        return r