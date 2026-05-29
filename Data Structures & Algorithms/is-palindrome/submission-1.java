class Solution {
    public boolean isPalindrome(String s) {
        String a = s;
        a = a.replaceAll("[^a-zA-Z0-9]", "");
        a = a.toLowerCase();
        char[] arr = a.toCharArray();
        char[] arr2 = new char[arr.length];

        int k = 0;
        for(int i = arr.length - 1; i >= 0; i--){
            arr2[k] = arr[i];
            k++;
        }

        for(int i = 0; i < arr.length; i++){
            if(arr[i] != arr2[i]){
                return false;
            }
        }

        return true;
    }
}
