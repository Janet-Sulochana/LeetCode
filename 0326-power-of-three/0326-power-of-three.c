bool isPowerOfThree(int n) {
    int i=0;
    if(n<1)return false;
    while(i<100)
    {
        if(n==1)return true;
        if(n%3!=0)return false;
        n=n/3;
        i++;
    }
    return false;

}