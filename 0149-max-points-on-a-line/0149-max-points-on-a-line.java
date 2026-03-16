class Solution {
    public int maxPoints(int[][] points) {
        int n=points.length;
        if(n<=2) return n;
        int result=0;
        for(int i=0;i<n;i++){
            Map<String,Integer> map=new HashMap<>();
            int max=0;
            for(int j=i+1;j<n;j++){
                int x=points[j][0]-points[i][0];
                int y=points[j][1]-points[i][1];
                if(x==0){
                    y=1;
                }
                else if(y==0){
                    x=1;
                }
                else{
                    int g=gcd(x,y);
                    x/=g;
                    y/=g;
                    if(x<0){
                        x=-x;
                        y=-y;
                    }
                }
                String key=x+","+y;
                map.put(key,map.getOrDefault(key,0)+1);
                max=Math.max(max,map.get(key));
            }
            result=Math.max(result,max+1);

        }
        return result;
    }
    private int gcd(int a,int b){
        a=Math.abs(a);
        b=Math.abs(b);
        if(b==0)return a;
        return gcd(b,a%b);
    }
}