class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s=str(num)
        c=0
        for i in range(len(s)-k+1):
            v=int(s[i:i+k])
            if v !=0 and num%v==0:
                c+=1
        return c