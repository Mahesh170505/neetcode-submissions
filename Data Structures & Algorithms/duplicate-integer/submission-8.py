class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Set = set()
        for i in range(len(nums)):
            Set.add(nums[i])
        if(len(Set) == len(nums)):
            return False
        return True