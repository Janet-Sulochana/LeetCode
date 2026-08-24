class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        x = ""
        for word in words:
            x += word
            if x == s:
                return True
            if len(x) > len(s):
                return False
        return False
