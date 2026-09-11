class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        ta=sum(apple)
        capacity.sort(reverse=True)
        for i , cap in enumerate(capacity):
            ta-=cap
            if ta<=0:
                return i+1
        return len(capacity)