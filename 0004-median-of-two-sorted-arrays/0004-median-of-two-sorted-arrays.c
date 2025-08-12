double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int n=nums1Size+nums2Size;
    int merged[n];
    int index=0,i=0,j=0;
    while(i<nums1Size && j<nums2Size)
    {
        if(nums1[i]<nums2[j])
        {
            merged[index++]=nums1[i];
            i++;
        }
        else
        {
            merged[index++]=nums2[j];
            j++;
        }
    }
    while(i<nums1Size)
    {
        merged[index++]=nums1[i];
        i++;
    }
    while(j<nums2Size)
    {
        merged[index++]=nums2[j];
        j++;
    }
    if(n%2==0)
    {
        return (merged[n/2-1]+merged[n/2])/2.0;
    }
    else
    {
        return merged[n/2];
    }
}