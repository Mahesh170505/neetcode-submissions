class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        List<int[]> array = new ArrayList<>();

        for(int i = 0; i < nums.length; i++){
            map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);
        }

        for(Map.Entry<Integer, Integer> entry: map.entrySet()){
            array.add(new int[]{entry.getValue(), entry.getKey()});
        }

        array.sort((a,b) -> b[0] - a[0]);
        int[] result = new int[k];
        for(int i = 0; i < k; i++){
            result[i] = array.get(i)[1];
        }
        return result;
    }
}
