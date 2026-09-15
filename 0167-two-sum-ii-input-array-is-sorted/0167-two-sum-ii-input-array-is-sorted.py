class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d={}
        for i,x in enumerate(numbers):
            if target-x in d:
                return d[target-x]+1,i+1
            d[x]=i