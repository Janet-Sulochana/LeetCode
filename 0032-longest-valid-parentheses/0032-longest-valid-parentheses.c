int longestValidParentheses(char* s) {
   int maxlen=0;
   int len=strlen(s);
   int stack[len+1];
   int top=-1;
   stack[++top]=-1;
   for(int i=0;i<len;i++)
   {
    if(s[i]=='(')
    {
        stack[++top]=i;
    }
    else
    {
        top--;
        if(top==-1)
        {
            stack[++top]=i;
        }
        else
        {
            int validlen=i-stack[top];
            if(validlen>maxlen)
            maxlen=validlen;
        }
    }
   }
   return maxlen;
}