class Solution {
    public int maxSubArray(int[] nums) {
        int n=nums.length;
        int maxEnd=0;
        int mSF=Integer.MIN_VALUE;
        for(int num:nums){
            maxEnd+=num;
            if(maxEnd>mSF){
                mSF=maxEnd;
            }
            if(maxEnd<0){
                maxEnd=0;
            }
        }
        return mSF;
    }
}