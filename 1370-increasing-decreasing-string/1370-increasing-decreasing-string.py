class Solution:
    def sortString(self, s: str) -> str:
        ans=""
        while s:
            for c in sorted(set(s)):
                ans+=c
                s=s.replace(c,"",1)
            for c in sorted(set(s), reverse=True):
                ans+=c
                s=s.replace(c,"",1)
        return ans