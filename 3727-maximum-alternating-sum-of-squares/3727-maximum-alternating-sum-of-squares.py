class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        arr=sorted([abs(x) for x in nums])
        n=len(arr)
        mid=n//2
        ans=0
        for i in range(mid):
            ans-=arr[i]**2
        for i in range(mid,n):
            ans+=arr[i]**2
        return ans