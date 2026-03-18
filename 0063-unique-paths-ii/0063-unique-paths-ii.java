class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int len=obstacleGrid[0].length;
        int[] table=new int[len];
        table[0]=1;
        for(int r[]:obstacleGrid){
            for(int j=0;j<len;j++){
                if(r[j]==1){
                    table[j]=0;
                }
                else if(j>0){
                    table[j]+=table[j-1];
                }
            }
        }
        return table[len-1];
    }
}