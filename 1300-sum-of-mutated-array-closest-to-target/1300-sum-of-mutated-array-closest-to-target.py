class Solution:
    def findBestValue(self, arr: list[int], target: int) -> int:
        arr.sort()
        n=len(arr)
        s=0
        if sum(arr)<=target:
            return arr[-1]
        for i in range(n):
            val=(target-s)//(n-i)
            if val<=arr[i]:
                if abs(target-(s+val*(n-i)))<=abs(target-(s+(val+1)*(n-i))):
                    return val
                return val+1
            s+=arr[i]
        return arr[-1]
        