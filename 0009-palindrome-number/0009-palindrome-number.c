bool isPalindrome(int x) {
    int temp,digit;
    long long rev=0;
    temp=x;
    while(x>0)
    {
        digit=x%10;
        rev=rev*10+digit;
        x/=10;
    }
    return temp==rev;
}