class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        result = []
        for num in nums:
            if(num in map):
                map[num] = map[num] + 1
            else:
                map[num] = 1
        sortMap = sorted(map.items(), key = lambda item: item[1], reverse = True)
        for i in range(k):
            result.append(sortMap[i][0])
        return result