class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        years=[0]*101
        for birth,death in logs:
            for year in range(birth,death):
                years[year-1950]+=1
        return 1950+years.index(max(years))