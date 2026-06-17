class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        j = 0
        result = [0] * len(nums)
        product = 1

        while(j < len(nums)):
            for i in range(len(nums)):
                if(i == j):
                    continue
                else:
                    product = product * nums[i]
            result[j] = product
            product = 1
            j = j + 1
        return result
                