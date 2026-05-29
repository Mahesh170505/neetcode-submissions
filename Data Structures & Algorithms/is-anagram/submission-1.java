class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }
        int [] newArray = new int[26]; // Setting a new array for s..
        for(int i = 0; i < newArray.length; i++){
            newArray[i] = 0;
        } // Initializing all the value inside the array to be zero..

        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            int j = c - 'a';
            newArray[j]++;
        } // Switching the select elements inside array to 1..

        int [] newArray2 = new int[26];
        for(int i = 0; i < t.length(); i++){
            char m = t.charAt(i);
            int j = m - 'a';
            newArray2[j]++;
        } // Switching the select elements inside array to 1..

        if(Arrays.equals(newArray, newArray2)){
            return true;
        }

        return false;
    }
}
