class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        r=s.split()
        res=[]
        for i in r:
            if i.isdigit():
                res.append(int(i))
        for i in range(1,len(res)):
            if res[i]<=res[i-1]:
                return False
        return True