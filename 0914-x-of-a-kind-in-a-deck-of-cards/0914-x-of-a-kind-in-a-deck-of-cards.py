from collections import Counter
from math import gcd
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count=Counter(deck)
        x=0
        for freq in count.values():
            x=gcd(x,freq)
        return x>=2