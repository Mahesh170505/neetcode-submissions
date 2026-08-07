class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        sort = sorted(nums)
        result = []
        for i in range(len(sort)):
            j = i + 1
            k = len(nums) - 1
            if(i > 0 and sort[i] == sort[i - 1]):
                continue
            else:
                while(j < k):
                    if(sort[j] + sort[k] + sort[i] > 0):
                        k -= 1
                    elif(sort[j] + sort[k] + sort[i] < 0):
                        j += 1
                    elif(sort[j] + sort[k] + sort[i] == 0):
                        result.append([sort[i], sort[j], sort[k]])
                        j += 1
                        k -= 1
                        while j < k and sort[j] == sort[j - 1]:
                            j += 1
                        while j < k and sort[k] == sort[k + 1]:
                            k -= 1
                    else:
                        continue
        return result