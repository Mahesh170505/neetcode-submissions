class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)
        result = [1] * k
        for i in range(len(nums)):
            num = nums[i]
            map[num] += 1
        sorted_map = dict(sorted(map.items(), key=lambda item: item[1], reverse=True))
        keys_list = list(sorted_map.keys())
        for i in range(k):
            result[i] = keys_list[i]
        return result
            
        