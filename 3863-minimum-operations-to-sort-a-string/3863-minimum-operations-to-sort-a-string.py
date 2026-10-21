class Solution:
    def minOperations(self, s: str) -> int:
        if list(s)==sorted(s):
            return 0
        n=len(s)
        if n==2:
            return -1
        mini=min(s)
        maxi=max(s)
        if s[0]==mini or s[-1]==maxi:
            return 1
        if mini in s[1:-1] or maxi in s[1:-1]:
            return 2
        return 3