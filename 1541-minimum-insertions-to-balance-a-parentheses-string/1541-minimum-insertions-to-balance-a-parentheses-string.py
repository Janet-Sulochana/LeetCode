class Solution:
    def minInsertions(self, s: str) -> int:
        o=0
        ans=0
        i=0
        while i<len(s):
            if s[i]=='(':
                o+=1
            else:
                if i+1<len(s) and s[i+1]==')':
                    i+=1
                else:
                    ans+=1
                if o>0:
                    o-=1
                else:
                    ans+=1
            i+=1
        return ans+2*o