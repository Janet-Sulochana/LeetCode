class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans=[]
        for i in range(len(s)):
            d=min(abs(i-j) for j in range(len(s))if s[j]==c)
            ans.append(d)
        return ans