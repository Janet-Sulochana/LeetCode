class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        d={}
        for i in range(n):
            if nums[i] in d:
                r=i-d[nums[i]]
                if r<=k:
                    return True
            d[nums[i]]=i
        return False