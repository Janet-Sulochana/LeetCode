class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        n=len(ages)
        ages.sort()
        l=0
        count=0
        r=0
        for age in ages:
            if age <= 14:
                continue
            while ages[l] <= 0.5 *age+7:
                l+=1
            while r+1<n and ages[r+1]<=age:
                r+=1
            count+=r-l
        return count