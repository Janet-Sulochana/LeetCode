class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count=ans=0
        for x in s:
            count+=1 if x=='L' else -1
            if count==0:
                ans+=1
        return ans