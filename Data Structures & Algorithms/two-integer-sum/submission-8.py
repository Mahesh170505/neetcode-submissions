class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()
        for i in range(len(nums)):
            num = nums[i]
            diff = target - num
            if diff in map:
                return [map.get(diff), i]
            else:
                map[num] = i
        return []