class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total=sum(nums)
        l=0
        ans=[]
        for x in nums:
            total-=x
            ans.append(abs(l-total))
            l+=x
        return ans