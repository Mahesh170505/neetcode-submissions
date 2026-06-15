class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set([])
        for num in nums:
            hashset.add(num)
        
        if(len(nums) != len(hashset)):
            return True
        
        return False
        