char* reverseWords(char* s) {
    char* words[10000];
    int count=0;

    char* copy=strdup(s);
    char* token=strtok(copy," ");
    while(token!=NULL){
        words[count++]=token;
        token=strtok(NULL," ");
    }
    char* result=(char*)malloc(strlen(s)+1);
    result[0]='\0';

    for(int i=count-1;i>=0;i--){
        strcat(result,words[i]);
        if(i!=0){
            strcat(result," ");
        }
    }
    free(copy);
    return result;
    
}