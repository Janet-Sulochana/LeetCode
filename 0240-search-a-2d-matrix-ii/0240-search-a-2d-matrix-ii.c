bool searchMatrix(int** matrix, int matrixSize, int* matrixColSize, int target){
    int x=*matrixColSize;
    int found=0;
    for(int i=0;i<matrixSize;i++)
    {
        for(int j=0;j<x;j++)
        {
            if(matrix[i][j]==target)
            {
                found=1;
                break;                
            }
            
        }
    }
    return found==1;
}