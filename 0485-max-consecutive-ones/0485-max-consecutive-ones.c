int findMaxConsecutiveOnes(int* nums, int numsSize) {
    int countMax=0;
    int count=0;
    for(int i=0;i<numsSize;i++){
        if(nums[i]==1){
            count++;
            if(count>countMax)countMax=count;
        }
        else
            count=0;
    }
    return countMax;
}