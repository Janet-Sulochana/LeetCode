class Solution {
    static int gcd(int a,int b){
        if(b==0){
            return a;
        }
        return gcd(b,a%b);
    }
    public int findGCD(int[] nums) {
        int min=Integer.MAX_VALUE;
        int max=Integer.MIN_VALUE;
        for(int n:nums){
            min=Math.min(min,n);
            max=Math.max(max,n);
        }
        return gcd(min,max);
    }
}