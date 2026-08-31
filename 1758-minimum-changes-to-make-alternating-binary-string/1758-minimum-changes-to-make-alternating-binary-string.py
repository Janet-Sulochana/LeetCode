class Solution:
    def minOperations(self, s: str) -> int:
        ops_start_0=sum(ch!=str(i%2) for i , ch in enumerate(s))
        return min(ops_start_0,len(s)-ops_start_0)