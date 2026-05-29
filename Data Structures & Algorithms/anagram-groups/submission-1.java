class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, Integer> myMap = new HashMap<>();
        List<List<String>> result = new ArrayList<>();

        for(int i = 0; i < strs.length; i++){
            String s = strs[i];
            char [] chars = s.toCharArray();
            Arrays.sort(chars);
            s = new String(chars);

            if(!myMap.containsKey(s)){
                myMap.put(s, result.size());
                result.add(new ArrayList<>());
            }
            result.get(myMap.get(s)).add(strs[i]);
        }
        return result;
    }
}
