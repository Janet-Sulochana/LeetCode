class Solution {
    public int[] nextGreaterElements(int[] nums) {
        int n=nums.length;
        int[] result=new int[n];
        Arrays.fill(result,-1);
        Stack<Integer> st=new Stack();
        for(int i=0;i<2*n;i++){
            int ind=i%n;
            while(!st.isEmpty()&&nums[ind]>nums[st.peek()]){
                int t1=st.pop();
                result[t1]=nums[ind];
            }
            if(i<n)
                st.push(ind);
        }
        return result;
    }
}