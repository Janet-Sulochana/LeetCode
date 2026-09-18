class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        a=float('inf')
        for ch in set(target):
            a=min(a,s.count(ch)//target.count(ch))
        return a