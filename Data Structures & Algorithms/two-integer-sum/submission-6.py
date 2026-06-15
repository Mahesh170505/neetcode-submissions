class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        result: List[int]
        for i, num in enumerate(nums):
            complement: int = target - num
            if(complement in hashmap):
                return [hashmap[complement], i]
            hashmap[num] = i
