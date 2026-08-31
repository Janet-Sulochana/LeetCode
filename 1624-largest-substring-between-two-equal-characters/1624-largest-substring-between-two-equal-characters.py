class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first_idx={}
        max_len=-1
        for i,ch in enumerate(s):
            if ch in first_idx:
                max_len=max(max_len,i-first_idx[ch]-1)
            else:
                first_idx[ch]=i
        return max_len