int minAddToMakeValid(char* s) {
    int open=0;
    int close=0;
    int len=strlen(s);
    for(int i=0;i<len;i++)
    {
        if(s[i]=='(')
        {
            open++;
        }
        else if(s[i]==')')
        {
            if(open>0)open--;
            else close++;
        }
    }
    return open+close;
}