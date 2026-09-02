from itertools import accumulate
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix=[0]+list(accumulate(arr,operator.xor))
        return [prefix[R+1]^prefix[L] for L,R in queries]