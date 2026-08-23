class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        a=set(allowed)
        count=0
        for i in words:
            w=set(i)
            if w<=a:
                count+=1
        return count