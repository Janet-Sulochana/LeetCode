bool checkPerfectNumber(int num) {
    
    int sum=0;
    int temp=num;
    for(int i=1;i<num;i++){
        if(num%i==0){
            sum+=i;
            if(sum>num)return false;
        }
    }
    if(temp==sum){
        return true;
    }
    return false;
}