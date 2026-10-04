class Solution:
    def checkValidString(self, s: str) -> bool:
        mino=0
        maxo=0
        for ch in s:
            if ch=='(':
                mino+=1
                maxo+=1
            elif ch == ')':
                mino-=1
                maxo-=1
            elif ch=='*':
                mino-=1
                maxo+=1
            if maxo<0:
                return False
            if mino<0:
                mino=0
        return mino==0