class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        n=len(word)
        if ch not in word:
            return word
        x=word.index(ch)
        a=word[:x+1]
        c=a[::-1]
        b=word[x+1:]
        return c+b