class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        
        output = []
        
        for i in range(len(nums)):
            j = i + 1
            k = len(sorted_nums) - 1
            Sum = 0 - sorted_nums[i]
            if(i == 0 or sorted_nums[i] != sorted_nums[i - 1]):
                while(j < k):
                    if(sorted_nums[j] + sorted_nums[k] < Sum):
                        j += 1
                    elif(sorted_nums[j] + sorted_nums[k] > Sum):
                        k -= 1
                    else:
                        triplet = [sorted_nums[i], sorted_nums[j], sorted_nums[k]]
                        j += 1
                        k -= 1
                        output.append(triplet)
                        while(j < k and sorted_nums[j] == sorted_nums[j - 1]):
                            j += 1
                        while(k > j and sorted_nums[k] == sorted_nums[k + 1]):
                            k -= 1
        return output
        