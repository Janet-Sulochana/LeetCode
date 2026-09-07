class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even=nums[::2]
        odd=nums[1::2]
        even.sort()
        odd.sort(reverse=True)
        ans=[]
        for i in range(len(nums)):
            if i%2==0:
                ans.append(even[i//2])
            else:
                ans.append(odd[i//2])
        return ans