bool isPowerOfFour(int n) {
    int i=0;
    if(n<1)return false;
    while(i<100)
    {
        if(n==1)return true;
        if(n%4!=0)return false;
        n=n/4;
        i++;
    }
    return false;
}