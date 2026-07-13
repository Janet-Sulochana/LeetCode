class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        n=len(g)
        m=len(s)
        i=0
        count=0
        for j in range(m):
            if i<n and g[i]<=s[j]:
                count+=1
                i+=1
        return count