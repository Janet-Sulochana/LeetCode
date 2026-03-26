class Solution {
    public int maximumUnits(int[][] boxTypes, int truckSize) {
        int maxUnits=0;
        Arrays.sort(boxTypes,(a,b)->b[1]-a[1]);
        for(int[] box : boxTypes){
            int boxes=box[0];
            int units=box[1];
            int take=Math.min(truckSize,boxes);
            maxUnits+=take*units;
            truckSize-=take;
            if(truckSize==0) break;
        }
        return maxUnits;
    }
}