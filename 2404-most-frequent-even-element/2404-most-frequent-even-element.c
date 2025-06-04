int mostFrequentEven(int* nums, int numsSize) {
    int evencounts[100001]={0};
    int maxfreq=0;
    int result=INT_MAX;
    for(int i=0;i<numsSize;i++)
    {
        if(nums[i]%2==0)
        {
            evencounts[nums[i]]++;
            if(evencounts[nums[i]]>maxfreq)
            {
                maxfreq=evencounts[nums[i]];
                result=nums[i];
            }
            else if(evencounts[nums[i]]==maxfreq&&nums[i]<result)
            {
                result=nums[i];
            }
        }
    }
    return (maxfreq==0)?-1:result;
}