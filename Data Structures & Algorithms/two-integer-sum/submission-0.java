class Solution {
    public int[] twoSum(int[] nums, int target) {
       Map<Integer, Integer> myMap = new HashMap<>();
       for(int i = 0; i < nums.length; i++){
        int num = nums[i];
        int complement = target - nums[i];
        if(myMap.containsKey(complement)){
            return new int[]{myMap.get(complement), i};
        }
        
            myMap.put(num, i);
       }
       return new int[]{};
    }
}
