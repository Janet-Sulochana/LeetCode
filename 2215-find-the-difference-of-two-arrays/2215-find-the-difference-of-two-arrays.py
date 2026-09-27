class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        l=[]
        a=[]
        for i in nums1:
            if i not in nums2 and i not in a:
                a.append(i)
        b=[]
        for j in nums2:
            if j not in nums1 and j not in b:
                b.append(j)
        l.append(a)
        l.append(b)
        return l
