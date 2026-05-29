class Solution {
    public boolean isAnagram(String s, String t) {
        char[] arr = s.toCharArray();
        char[] arr2 = t.toCharArray();
        int [] nums = new int[26];
        int [] nums2 = new int[26];

        if(arr.length != arr2.length){
            return false;
        }
        for(int i = 0; i < arr.length; i++){
            int num = arr[i] - 'a';
            nums[num]++;
        }

        for(int j = 0; j < arr2.length; j++){
            int num = arr2[j] - 'a';
            nums[num]--;
        }

        for(int num : nums){
            if(num != 0){
                return false;
            }
        }
        return true;
    }
}
