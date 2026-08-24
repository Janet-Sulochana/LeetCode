class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans=[]
        for n in range(left,right+1):
            if all(int(x)!=0 and n%int(x)==0 for x in str(n)):
                ans.append(n)
        return ans