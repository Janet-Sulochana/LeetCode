class Solution:
    def greatestLetter(self, s: str) -> str:
        c=set(s)
        for ch in "ZYXWVUTSRQPONMLKJIHGFEDCBA":
            if ch in c and ch.lower() in c:
                return ch
        return ""