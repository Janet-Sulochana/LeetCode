double findMaxAverage(int* nums, int numsSize, int k) {
    int sum=0;
    for(int i=0;i<k;i++)
    {
        sum+=nums[i];
    }
    double maxavg=(double)sum/k;
    double avg=0;
    for(int i=k;i<numsSize;i++)
    {
        sum=sum-nums[i-k]+nums[i];
        avg=(double)sum/k;
        if(avg>maxavg)
        {
            maxavg=avg;
        }
    }

    return maxavg;
}