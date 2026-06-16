class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        count = [[] for i in range(len(nums) + 1)]
        for num in nums:
            map[num] = map.get(num, 0) + 1
        for num, i in map.items():
            count[i].append(num)
        
        result = []
        for i in range(len(count) - 1, 0, -1):
            for num in count[i]:
                result.append(num)
                if len(result) == k:
                    return result