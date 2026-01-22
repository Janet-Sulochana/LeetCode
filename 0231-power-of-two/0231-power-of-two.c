bool isPowerOfTwo(int n) {
    if(n<=0)return false;
    int i=0;
    while(i<100){
        if(n==1)return true;
        if(n%2!=0)return false;
        n/=2;
        i++;
    }
    return false;
}