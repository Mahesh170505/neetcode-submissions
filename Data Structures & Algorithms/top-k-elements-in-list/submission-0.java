class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        List<Integer>[] array = new List[nums.length + 1];
        HashMap<Integer, Integer> myMap = new HashMap<>();

        for(int i = 0; i < array.length; i++){
            array[i] = new ArrayList<>();
        }

        for(int i = 0; i < nums.length; i++){
            myMap.put(nums[i], myMap.getOrDefault(nums[i], 0) + 1);
        }

        

        for(Map.Entry<Integer, Integer> entry : myMap.entrySet()){
            array[entry.getValue()].add(entry.getKey());
        }

        int [] result = new int [k];
        int index = 0;

        for(int i = array.length - 1; index < k && i > 0; i--){
            for(int j : array[i]){
                result[index++] = j;
                
                if(index == k){
                    return result;
                }
            }
        }
        return result;
    }
}
