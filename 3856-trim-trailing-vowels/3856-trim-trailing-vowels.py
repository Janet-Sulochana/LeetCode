class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        vowels="aeiou"
        return s.rstrip(vowels)