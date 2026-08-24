class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
      Map<String,List<String>> map = new HashMap<>();
      for(String i:strs){
        char[] c = i.toCharArray();
        Arrays.sort(c);
        String key = new String(c);
        if(!map.containsKey(key)){
            map.put(key,new LinkedList<>());
        }
        map.get(key).add(i);
      }
     // System.out.println(map);
      return new ArrayList<>(map.values());
        
    }
}