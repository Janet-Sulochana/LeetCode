class Solution {
    public String[] findRestaurant(String[] list1, String[] list2) {
        int minIndex=Integer.MAX_VALUE;
        List<String> iLast=new ArrayList<>();
        for(int i=0;i<list1.length;i++){
            int sumIndex=0;
            for(int j=0;j<list2.length;j++){
                if(list1[i].equals(list2[j])){
                    sumIndex=i+j;
                    if(sumIndex<minIndex){
                        minIndex=sumIndex;
                        iLast.clear();
                        iLast.add(list1[i]);
                    }
                    else if(sumIndex==minIndex){
                        iLast.add(list1[i]);
                    }
                
                }
            
            }
        }
        return iLast.toArray(new String[0]);
    }
}