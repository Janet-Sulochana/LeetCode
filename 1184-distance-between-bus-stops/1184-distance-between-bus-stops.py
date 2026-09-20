class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start>destination:
            start,destination=destination,start
        c_d=sum(distance[start:destination])
        t_d=sum(distance)
        return min(c_d,t_d-c_d)