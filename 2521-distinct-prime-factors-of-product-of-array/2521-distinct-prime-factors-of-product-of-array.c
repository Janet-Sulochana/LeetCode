int distinctPrimeFactors(int* nums, int numsSize) {
    int count=0;
    bool prime_factors[1001]={false};
    for(int i=0;i<numsSize;i++)
    {
        int num=nums[i];
        if(num<2)
        {
            continue;
        }
        if(num%2==0)
        {
            if(!prime_factors[2])
            {
                prime_factors[2]=true;
                count++;
            }
            while(num%2==0)
            {
                num/=2;
            }
        }
        for(int p=3;p*p<=num;p+=2)
        {
            if(num%p==0)
            {
                if(!prime_factors[p])
                {
                    prime_factors[p]=true;
                    count++;
                }
                while(num%p==0)
                {
                    num/=p;
                }
            }
        }
        if(num>2)
        {
            if(!prime_factors[num])
            {
                prime_factors[num]=true;
                count++;
            }
        }
    }
    return count;
}