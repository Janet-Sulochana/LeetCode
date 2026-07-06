class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n=len(people)
        l=0
        r=n-1
        count=0
        while l<=r:
            if people[l]+people[r]<=limit:
                l+=1
            r-=1
            count+=1
        return count
            