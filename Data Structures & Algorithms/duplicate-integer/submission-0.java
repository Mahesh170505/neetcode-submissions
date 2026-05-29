class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> mySet = new HashSet<>();
        for(int i = 0; i < nums.length; i++){
            mySet.add(nums[i]);
        }
        if(mySet.size() != nums.length){
            return true;
        }
        return false;
    }
}