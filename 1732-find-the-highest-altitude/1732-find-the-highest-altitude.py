class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        height=ans=0
        for x in gain:
            height+=x
            ans=max(ans,height)
        return ans