char* longestCommonPrefix(char** strs, int strsSize) {
    if(strsSize==0)return "";
    char *result=(char*)malloc(200 * sizeof(char));
    int k=0;
    for(int j=0;strs[0][j] != '\0';j++){
        for(int i=1;i<strsSize;i++){
            if(strs[i][j]!=strs[0][j]){
                result[k]='\0';
                return result;
            }
        }
        result[k++]=strs[0][j];
    }
    result[k]='\0';
    return result;
}