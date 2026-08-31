from typing import List
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        s=paragraph.lower().split()
        c=0
        d={}
        for i in s:
            new=""
            for ch in i:
                if ch.isalpha():
                    new+=ch
                else:
                    new+=" "
            i=i.strip("',;.!?")
            for i in new.split():
                if i not in banned:
                    d[i]=d.get(i,0)+1
        return max(d,key=d.get)