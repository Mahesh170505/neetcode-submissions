class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }
        int [] count = new int[26];

        for(char c : s.toCharArray()){
            int index = c - 'a';
            count[index]++;
        }
        
        for(char c: t.toCharArray()){
            int index = c - 'a';
            count[index]--;
        }

        for(int i = 0; i < count.length; i++){
            if(count[i] != 0){
                return false;
            }
        }
        return true;
    }
}
