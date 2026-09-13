class Solution:
    def isFascinating(self, n: int) -> bool:
        c=str(n)+str(2*n)+str(3*n)
        return "".join(sorted(c))=="123456789"