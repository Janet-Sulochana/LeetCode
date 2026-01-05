int mySqrt(int x) {
    int n=x;
    if(n<0)return -1;
    if(n==0||n==1)return n;
    int ans=0;
    int low=1,high=n;
    while(low<=high)
    {
        double mid=low+(high-low)/2;
        double square=mid*mid;
        if(square==n)
        {
            return (int)mid;
        }
        else if(square<n)
        {
            low=mid+1;
            ans=(int)mid;
        }
        else
        {
            high=mid-1;
        }
    }
    return ans;
}