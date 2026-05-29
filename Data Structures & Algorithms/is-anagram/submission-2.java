class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }

        int [] arr = new int[26];
        char [] c = s.toCharArray();
        char [] d = t.toCharArray();
        int [] arr2 = new int[26];

        for(int i = 0; i < arr.length; i++){
            arr[i] = 0;
        }

        for(int i = 0; i < c.length; i++){
            int j = c[i] - 'a';
            arr[j]++;
        }

        for(int i = 0; i < d.length; i++){
            int k = d[i] - 'a';
            arr2[k]++;
        }

        return Arrays.equals(arr,arr2);
    }
}
