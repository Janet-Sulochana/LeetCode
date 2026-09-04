class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        def reflection(i):
            s=bin(i)[2:]
            s=s[::-1]
            return int(s,2)
        nums.sort(key= lambda x:(reflection(x),x))
        return nums