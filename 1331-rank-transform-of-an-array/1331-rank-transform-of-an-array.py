class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        s=sorted(set(arr))
        rank={}
        r=1
        for i in s:
            rank[i]=r
            r+=1
        res=[]
        for i in arr:
            res.append(rank[i])
        return res