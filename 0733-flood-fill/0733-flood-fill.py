class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        old=image[sr][sc]
        if old==color:
            return image
        q=deque([(sr,sc)])
        image[sr][sc]=color
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            r,c=q.popleft()
            for dr,dc in directions:
                nr=r+dr
                nc=c+dc
                if(0<=nr<len(image) and 0<=nc<len(image[0]) and image[nr][nc]==old):
                    image[nr][nc]=color
                    q.append((nr,nc))
        return image