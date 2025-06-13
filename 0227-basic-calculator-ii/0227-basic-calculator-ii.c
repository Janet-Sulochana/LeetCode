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
            switch(op)
            {
                case '+':
                result+=temp;
                temp=num;
                break;
                case '-':
                result+=temp;
                temp=-num;
                break;
                case '*':
                temp*=num;
                break;
                case '/':
                temp/=num;
                break;
            }
            op=c;
            num=0;
        }    
    }
    return result+temp;
}