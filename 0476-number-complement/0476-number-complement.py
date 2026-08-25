class Solution:
    def findComplement(self, num: int) -> int:
        b=bin(num)[2:]
        ans=''.join('1' if x =='0' else '0' for x in b)
        return int(ans,2)