class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i: int = 0
        j: int = len(numbers) - 1
        output = []
        
        while i < j:
            total = numbers[i] + numbers[j]
            if(total < target):
                i+=1
            elif(total > target):
                j-=1
            else:
                return [i + 1, j + 1]
        
   