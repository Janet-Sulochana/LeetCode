class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result =new ArrayList<>();
        int n=nums.length;
        Arrays.sort(nums);
        for(int i=0;i<n-2;i++){
            for(int j=i+1;j<n-1;j++){
                for(int k=j+1;k<n;k++){
                    if(nums[i]+nums[j]+nums[k]==0){
                        List<Integer> temp=Arrays.asList(nums[i],nums[j],nums[k]);
                        if(!result.contains(temp)){
                            result.add(temp);
                        }
                    }
                }
            }
        }
        return result;
    }
}