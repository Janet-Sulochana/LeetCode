class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        durations=[releaseTimes[0]]+[releaseTimes[i]-releaseTimes[i-1] for i in range(1,len(releaseTimes))]
        return max(zip(durations,keysPressed))[1]