class NumArray:

    def __init__(self, nums: list[int]):
        self.size=len(nums)
        self.stree=[0]*(4*self.size)
        self.nums=nums
        if self.size>0:
            self.build(1,0,self.size-1)
    
    def build(self,node,start,end):
        if start==end:
            self.stree[node]=self.nums[start]
            return
        mid=(start+end)//2
        self.build(node*2,start,mid)
        self.build(node*2+1,mid+1,end)
        self.stree[node]=(self.stree[node*2]+self.stree[(node*2)+1])

    def update(self, index: int, val: int) -> None:
        def updateTree(node,start,end):
            if start==end:
                self.stree[node]=val
                return
            mid=(start+end)//2
            if index<=mid:
                updateTree(node*2,start,mid)
            else:
                updateTree(node*2+1,mid+1,end)
            self.stree[node]=(self.stree[node*2]+self.stree[node*2+1])
        updateTree(1,0,self.size-1)


    def sumRange(self, left: int, right: int) -> int:
        def sumTree(node,start,end):
            if right<start or end<left:
                return 0
            if left<=start and end<=right:
                return self.stree[node]
            mid=(start+end)//2
            return sumTree(node*2,start,mid)+sumTree(node*2+1,mid+1,end)
        return sumTree(1,0,self.size-1)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)