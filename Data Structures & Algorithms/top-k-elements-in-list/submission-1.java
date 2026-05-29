class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        List<Integer>[] myArray = new List[nums.length + 1];
        HashMap<Integer, Integer> myMap = new HashMap<>();

        //Filling the array with correct placeholders in each element..
        for(int i = 0; i < myArray.length; i++){
            myArray[i] = new ArrayList<>();
        } 

        //Filling the hashMap with correct elements, and updating the key/value..
        for(int i = 0; i < nums.length; i++){
            myMap.put(nums[i], myMap.getOrDefault(nums[i], 0) + 1);
        }

        //Filling the array we made with respect to our hashMap..
        for(Map.Entry<Integer, Integer> entry : myMap.entrySet()){
            myArray[entry.getValue()].add(entry.getKey());
        }

        int [] result = new int [k];
        int index = 0;

        for(int i = myArray.length - 1; i > 0 && index < k; i--){
            for(int n : myArray[i]){
                result[index] = n;
                index++;

                if(index == k){
                    return result;
                }
            }
        }
        return result;
    }
}
