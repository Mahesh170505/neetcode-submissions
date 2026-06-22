class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        result: int = 1
        current: int = 1
        nums.sort()

        for i in range(len(nums) - 1):
            if(nums[i] == nums[i + 1]):
                continue
            elif(nums[i + 1] == nums[i] + 1):
                current += 1
                result = max(result, current)
            else:
                current = 1
        return result