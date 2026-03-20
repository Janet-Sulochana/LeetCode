class Solution {
    public int candy(int[] ratings) {
        int n=ratings.length;
        int tc=n;
        int i=1;
        while(i<n){
            if(ratings[i]==ratings[i-1]){
                i++;
                continue;
            }
            int cp=0;
            while(i<n&&ratings[i]>ratings[i-1]){
                cp++;
                tc+=cp;
                i++;
            }
            if(i==n)return tc;
            int cv=0;
            while(i<n&&ratings[i]<ratings[i-1]){
                cv++;
                tc+=cv;
                i++;
            }
            tc-=Math.min(cp,cv);
        }
        return tc;
    }
}