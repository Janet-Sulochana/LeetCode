void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n) {
    int size=m+n;
    int *result=(int*)malloc(size * sizeof(int));
    int i=0,j=0,index=0;
    while(i<m && j<n)
    {
        if(nums1[i]<nums2[j])
        {
            result[index]=nums1[i];
            index++;
            i++;
        }
        else
        {
            result[index]=nums2[j];
            index++;
            j++;
        }
    }
    while(i<m)
    {
        result[index]=nums1[i];
        index++;
        i++;
    }
    while(j<n)
    {
        result[index]=nums2[j];
        index++;
        j++;
    }
    for(int i=0;i<size;i++)
    {
        nums1[i]=result[i];
    }
}