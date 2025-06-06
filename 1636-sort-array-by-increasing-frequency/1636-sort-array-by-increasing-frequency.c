/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* frequencySort(int* nums, int numsSize, int* returnSize) {
    *returnSize=numsSize;
    int *result=(int*)malloc(numsSize * sizeof(int));
    int *frequencies=(int*)malloc(numsSize * sizeof(int));
    int *values=(int*)malloc(numsSize * sizeof(int));
    int uniquecount=0;
    for(int i=0;i<numsSize;i++)
    {
        int found=0;
        for(int j=0;j<uniquecount;j++)
        {
            if(nums[i]==values[j])
            {
                frequencies[j]++;
                found=1;
                break;
            }
        }
        if(!found)
        {
            values[uniquecount]=nums[i];
            frequencies[uniquecount]=1;
            uniquecount++;
        }
        for(int i=0;i<uniquecount;i++)
        {
            for(int j=i+1;j<uniquecount;j++)
            {
                if(frequencies[i]>frequencies[j])
                {
                    int tempfreq=frequencies[i];
                    frequencies[i]=frequencies[j];
                    frequencies[j]=tempfreq;
                    int tempval=values[i];
                    values[i]=values[j];
                    values[j]=tempval;                
                }
                else if(frequencies[i]==frequencies[j])
                {
                    if(values[i]<values[j])
                    {
                        int tempval=values[i];
                        values[i]=values[j];
                        values[j]=tempval;
                    }
                }
            }
        }
    }
    int index=0;
    for(int i=0;i<uniquecount;i++)
    {
        for(int j=0;j<frequencies[i];j++)
        {
            result[index]=values[i];
            index++;
        }
    }
    free(frequencies);
    free(values);
    return result;
}