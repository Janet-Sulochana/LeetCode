class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits=[int(x) for x in str(n)]
        return __import__('math').prod(digits)-sum(digits)