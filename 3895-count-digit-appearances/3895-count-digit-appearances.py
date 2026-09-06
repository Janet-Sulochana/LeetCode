class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        res=""
        for i in nums:
            res+=str(i)
        return res.count(str(digit))