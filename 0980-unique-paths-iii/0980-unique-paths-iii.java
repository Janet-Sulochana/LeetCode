class Solution {
    public static int  DFS(int grid[][] , int i , int j , int ex , int ey ,int m , int n , int stepC , int counter){
        if(i < 0  || j < 0 || i >=m || j >= n){
            return 0;
        }
        if(i == ex && j == ey){
            if(counter == stepC){
                return 1;
            }
            else{
                return 0;
            }
        }
        if(grid[i][j] == -1){
            return 0;
        }
        if(grid[i][j]== 0){
            counter++;
        }
        int temp = grid[i][j];
        grid[i][j] = -1;
        int up = DFS(grid,i - 1 , j , ex , ey ,m , n , stepC ,counter);
        int down = DFS(grid,i + 1 , j , ex , ey ,m , n , stepC ,counter);
        int left = DFS(grid,i , j - 1 , ex , ey ,m , n , stepC ,counter);
        int right = DFS(grid,i , j + 1 , ex , ey ,m , n , stepC,counter);
        // backtracking
        grid[i][j] = temp;
        return up + down + left + right;
    }
    public int uniquePathsIII(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int sx = -1;
        int sy = -1;
        int ex = -1;
        int ey =  -1;
        int stepC = 0;
        for(int i = 0 ; i < m ; i++){
            for(int j = 0 ; j < n ; j++ ){
                if(grid[i][j] == 1){
                    sx = i;
                    sy = j;
                }
                if(grid[i][j] == 2){
                    ex = i;
                    ey = j;
                }
                if(grid[i][j]== 0){
                    stepC++;
                }
            }
        }
        int result = DFS(grid , sx , sy , ex , ey ,m , n , stepC , 0);
        return result;
        
    }
}