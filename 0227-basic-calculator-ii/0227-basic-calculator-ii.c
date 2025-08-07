int calculate(char* s) {
    int len=strlen(s);
    int result=0,num=0,temp=0;
    char op='+';
    for(int i=0;i<len;i++)
    {
        char c=s[i];
        if(isdigit(c))
        {
            num=num*10+(c-'0');
        }
        if(!isdigit(c) && c!=' ' || i==len-1)
        {
            if(op=='+' || op=='-')
            {
                result+=temp;
                temp=(op=='+')?num:-num;
            }
            else if(op=='*') temp*=num;
            else if(op=='/') temp/=num;
            op=c;
            num=0;
        }    
    }
    return result+temp;
}