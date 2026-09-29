class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> list[int]:
        jumbo_num=tomatoSlices-2*cheeseSlices
        if jumbo_num<0 or jumbo_num%2!=0:
            return []
        total_jumbo=jumbo_num//2
        total_small=cheeseSlices-total_jumbo
        if total_small<0:
            return []
        return [total_jumbo,total_small]
