class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels=set("aeiouAEIOU")
        mid=len(s)//2
        count_a=sum(1 for ch in s[:mid] if ch in vowels)
        count_b=sum(1 for ch in s[mid:] if ch in vowels)
        return count_a==count_b