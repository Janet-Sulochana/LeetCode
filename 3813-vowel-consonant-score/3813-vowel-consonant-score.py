class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        v=0
        c=0
        vowels="aeiou"
        for i in s:
            if i.isalpha():
                if i in vowels:
                    v+=1
                else:
                    c+=1
        return v//c if c>0 else 0