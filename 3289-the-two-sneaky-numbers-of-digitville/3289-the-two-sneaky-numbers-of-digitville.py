class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        s=set()
        sn=[]
        for num in nums:
            if num in s:
                sn.append(num)
            else:
                s.add(num)
            if len(sn)==2:
                break
        return sn