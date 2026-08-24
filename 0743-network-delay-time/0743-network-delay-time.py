import heapq
from typing import List
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=[[] for _ in range(n+1)]
        for u,v,w in times:
            graph[u].append((v,w))
        pq=[(0,k)]
        dist=[float('inf')]*(n+1)
        dist[k]=0
        while pq:
            d,node=heapq.heappop(pq)
            if d>dist[node]:
                continue
            for nei , weight in graph[node]:
                new_dist=d+weight
                if new_dist<dist[nei]:
                    dist[nei]=new_dist
                    heapq.heappush(pq,(new_dist,nei))
        if float('inf') in dist[1:]:
                return -1
        return max(dist[1:])