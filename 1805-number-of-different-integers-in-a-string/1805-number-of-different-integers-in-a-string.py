class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        res=[]
        i=0
        while i <len(word):
            if word[i].isdigit():
                r=""
                while i<len(word) and word[i].isdigit():
                    r+=word[i]
                    i+=1
                res.append(int(r))
            else:
                i+=1
        return len(set(res))
