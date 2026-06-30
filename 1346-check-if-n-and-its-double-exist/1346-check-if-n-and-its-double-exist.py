class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        n = len(arr)
        for i in range(n):
            target=2*arr[i]
            l=0
            r=n-1
            while l<=r:
                mid=(l+r)//2
                if arr[mid]==target and mid != i:
                    return True
                elif arr[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
        return False