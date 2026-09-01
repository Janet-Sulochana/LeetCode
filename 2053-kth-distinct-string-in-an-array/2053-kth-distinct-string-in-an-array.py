class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        res=[]
        for i in arr:
            if arr.count(i)>1:
                continue
            res.append(i)
        if len(res)<k:
            return ""
        return res[k-1]