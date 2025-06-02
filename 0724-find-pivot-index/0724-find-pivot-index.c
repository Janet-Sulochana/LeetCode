int pivotIndex(int* nums, int numsSize) {
   for(int i=0;i<numsSize;i++)
   {
    int leftsum=0,rightsum=0;
    for(int j=0;j<i;j++)
    {
        leftsum +=nums[j];
    }
    for(int k=i+1;k<numsSize;k++)
    {
        rightsum+=nums[k];
    }
    if(leftsum==rightsum)
    {
        return i;
    }
   }
   return -1;
}