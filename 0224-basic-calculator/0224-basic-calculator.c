int calculate(char* s) {
    int len=strlen(s);
    int result=0,num=0,sign=1;
    for(int i=0;i<len;i++)
    {
        char c=s[i];
        if(isdigit(c))
        {
            num=num*10+(c-'0');
        }
        else if(c=='+')
        {
            result+=sign*num;
            sign=1;
            num=0;
        }
        else if(c=='-')
        {
            result+=sign*num;
            sign=-1;
            num=0;
        }
        else if(c=='(')
        {
            int balance=1;
            int j=i+1;
            while(j<len && balance>0)
            {
                if(s[j]=='(')balance++;
                else if(s[j]==')')balance--;
                j++;
            }
            char temp=s[j-1];
            s[j-1]='\0';
            num=calculate(s+i+1);
            s[j-1]=temp;
            i=j-1;
        }
        else if(c==')')
        {
            result+=sign*num;
            return result;
        }
    }
    result+=sign*num;
    return result;
}