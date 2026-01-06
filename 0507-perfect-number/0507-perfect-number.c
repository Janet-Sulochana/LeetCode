bool checkPerfectNumber(int num) {
    if(num<=1)return true;
    int sum=1;
    int temp=num;
    for(int i=2;i*i<=num;i++){
        if(num%i==0){
            sum+=i;
            if(i!=num/i){
                sum+=num/i;
            }
        }
    }
    if(temp==sum){
        return true;
    }
    return false;
}