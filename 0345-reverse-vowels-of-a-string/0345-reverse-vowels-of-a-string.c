char* reverseVowels(char* s) {
    int r=strlen(s)-1;
    int f=0;
    while(f<r)
    {
        char ch=tolower(s[f]);
        char ch1=tolower(s[r]);
        if(ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u')
        {
            if(ch1=='a'||ch1=='e'||ch1=='i'||ch1=='o'||ch1=='u')
            {
                char temp=s[r];
                s[r]=s[f];
                s[f]=temp;
                f++;r--;
            }
            else 
            {
                r--;
            }
        }
        else
            {
                f++;
            }
    }
    return s;
}