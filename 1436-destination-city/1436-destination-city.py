class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start={x[0] for x in paths}
        for a,b in paths:
            if b not in start:
                return b