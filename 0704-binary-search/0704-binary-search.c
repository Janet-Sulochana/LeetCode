int search(int* nums, int numsSize, int target) {
    int low=0,high=numsSize-1,mid;
    if(numsSize==1 || numsSize==2|| numsSize==3)
    {
        for(int i=0;i<numsSize;i++)
        {
            if(nums[i]==target)
            {
                return i;
            }
        }
    }
    while(low<=high)
    {
        mid=(low+high)/2;
        if(nums[mid]==target)
        {
            return mid;
        }
        if(nums[mid]<target)
        {
            low=mid+1;
        }
        else
        {
            high=mid-1;
        }
    }
    return -1;
}