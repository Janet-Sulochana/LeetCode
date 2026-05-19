class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if 0 in nums:
            l=[]
            for i in range(len(nums)):
                prod=1
                for j in range (len(nums)):
                    if i!=j:
                        prod*=nums[j]
                l.append(prod)
            return l
        else:
            l=[]
            prod=1
            for i in range(len(nums)):
                prod*=nums[i]
            for i in nums:
                l.append(prod//i)
            return l