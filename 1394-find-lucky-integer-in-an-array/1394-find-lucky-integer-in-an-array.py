
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        n=set(arr)
        max_v=0
        for i in n:
            if arr.count(i)==i:
                max_v=max(max_v,i)
        if max_v:
            return max_v
        return -1