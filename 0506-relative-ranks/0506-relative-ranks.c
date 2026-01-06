/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int cmp(const void* a,const void* b){
    return (*(int*)b-*(int*)a);
 }
char** findRelativeRanks(int* score, int scoreSize, int* returnSize) {
    char** answer=(char**)malloc(sizeof(char*)*scoreSize);
    *returnSize=scoreSize;
    int temp[scoreSize];
    for(int i=0;i<scoreSize;i++){
        temp[i]=score[i];
    }
    qsort(temp,scoreSize,sizeof(int),cmp);
    for(int i=0;i<scoreSize;i++){
        int rank;
        for(rank=0;rank<scoreSize;rank++){
            if(score[i]==temp[rank]){
                break;
            }
        }
        if(rank==0)answer[i]="Gold Medal";
        else if(rank==1)answer[i]="Silver Medal";
        else if(rank==2)answer[i]="Bronze Medal";
        else{
            answer[i]=(char*)malloc(12);
            sprintf(answer[i],"%d",rank+1);

        }
    }
    return answer;
}