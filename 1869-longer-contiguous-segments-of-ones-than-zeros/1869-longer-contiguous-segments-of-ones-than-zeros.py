class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        max_ones=curr_ones=0
        max_zeros=curr_zeros=0
        for ch in s:
            if ch=="1":
                curr_ones+=1
                curr_zeros=0
            else:
                curr_zeros+=1
                curr_ones=0
            max_ones=max(max_ones,curr_ones)
            max_zeros=max(max_zeros,curr_zeros)
        return max_ones>max_zeros