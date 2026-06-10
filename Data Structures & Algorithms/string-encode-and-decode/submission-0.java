class Solution {

    public String encode(List<String> strs) {
        StringBuilder result = new StringBuilder();
        for(int i = 0; i < strs.size(); i++){
            result.append(strs.get(i).length()).append("#").append(strs.get(i));
        }
        return result.toString();
    }

    public List<String> decode(String str) {
        List<String> result = new ArrayList<>();
        int i = 0; 
        while(i < str.length()){
            int j = i;
            while(str.charAt(j) != '#'){
                j++;
            }
            int length = Integer.parseInt(str.substring(i,j));
            i = j + 1;
            j = i + length;
            result.add(str.substring(i, j));
            i = j;
        }
        return result;
    }
}
