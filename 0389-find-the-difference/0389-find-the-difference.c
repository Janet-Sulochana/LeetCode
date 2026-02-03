char findTheDifference(char* s, char* t) {
    int lens=strlen(s);
    int lent=strlen(t);
    char extra;
    if(lens==0)
    {
        lens=1;
    }
    for(int i=0;i<lens;i++)
    {
        int found=0;
        for(int j=0;j<lent;j++)
        {
            if(s[i]!=t[j])
            {
                found=1;
                extra=t[j];
            }
        }
    }
    return extra;
}