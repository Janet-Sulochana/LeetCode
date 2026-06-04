class Solution {
    public boolean checkVowels(char c){
        return c=='a'||c=='e'||c=='o'||c=='i'||c=='u';
    }
    public int maxVowels(String s, int k) {
        int n=s.length();
        int maxV=0;
        for(int i=0;i<k;i++){
            if(checkVowels(s.charAt(i))){
                maxV++;
            }
        }
        int curW=maxV;
        for(int i=k;i<n;i++){
            if(checkVowels(s.charAt(i))){
                curW++;
            }
            if(checkVowels(s.charAt(i-k))){
                curW--;
            }
            maxV=Math.max(maxV,curW);
            
        }
        return maxV;
    }
}