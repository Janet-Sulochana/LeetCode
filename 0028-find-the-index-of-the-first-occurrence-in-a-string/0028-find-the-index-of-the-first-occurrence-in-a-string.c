int strStr(char* haystack, char* needle) {
    char *s=strstr(haystack,needle);
    if(s!=NULL)
    {return s-haystack;}
    return -1;}