class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int n=gas.length;
        long tc=0;
        long tg=0;
        for(int i=0;i<n;i++){
            tc+=cost[i];
            tg+=gas[i];
        }
        if(tg<tc)return -1;
        int index=0;
        int spend=0;
        for(int i=0;i<n;i++){
            spend+=(gas[i]-cost[i]);
            if(spend<0){
                index=i+1;
                spend=0;
            }
        }
        return index;
    }
}