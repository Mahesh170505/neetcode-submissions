class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, Comparator.comparingInt(i -> i[1]));
        int prev_interval = 0;
        int count = 1;

        for(int i = 1; i < intervals.length; i++){
            if(intervals[i][0] >= intervals[prev_interval][1]){
                count++;
                prev_interval = i;
            }
        }
        return intervals.length - count;
    }
}
