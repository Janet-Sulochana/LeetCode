/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* intersection(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize) {
    int *result=(int*)malloc(((nums1Size<nums2Size)?nums1Size:nums2Size) * sizeof(int));
    int index=0;
    for(int i=0;i<nums1Size;i++)
    {
        for(int j=0;j<nums2Size;j++)
        {
            if(nums1[i]==nums2[j])
            {
               int found=0;
               for(int k=0;k<index;k++)
               {
                if(result[k]==nums1[i])
                {
                    found=1;
                    break;
                }
               }
               if(!found)
                {
                    result[index++]=nums1[i];
                }
               break;
            }
        }
    }
    *returnSize=index;
    return result;
}