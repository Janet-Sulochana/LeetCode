class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        arr = []
        for i, num in enumerate(nums):
            s = 0
            n = num
            while n > 0:
                s += n % 10
                n //= 10
            arr.append((s, num, i))
        arr.sort()
        vis = [False] * len(nums)
        swaps = 0
        for i in range(len(nums)):
            if vis[i] or arr[i][2] == i:
                continue
            j = i
            cycle = 0
            while not vis[j]:
                vis[j] = True
                j = arr[j][2]
                cycle += 1
            swaps += cycle - 1
        return swaps

