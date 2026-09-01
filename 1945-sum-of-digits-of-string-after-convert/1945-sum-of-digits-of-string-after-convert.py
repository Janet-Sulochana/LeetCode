class Solution:
    def getLucky(self, s: str, k: int) -> int:
        total=sum(int(digit) for ch in s for digit in str(ord(ch)-ord('a')+1))
        for _ in range(k-1):
            total=sum(int(digit) for digit in str(total))
        return total