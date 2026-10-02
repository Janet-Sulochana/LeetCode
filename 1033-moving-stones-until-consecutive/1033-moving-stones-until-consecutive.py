class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> list[int]:
        x,y,z=sorted([a,b,c])
        if z-x==2:
            min_m=0
        elif y-x<=2 or z-y<=2:
            min_m=1
        else:
            min_m=2
        max_m=(z-x-2)
        return [min_m,max_m]