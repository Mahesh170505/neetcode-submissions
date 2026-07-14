class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i in range(len(temperatures)):
            j = i + 1
            count = 0
            found = False
            while(j <= len(temperatures) - 1):
                if(temperatures[j] > temperatures[i]):
                    found = True
                    count += 1
                    result.append(count)
                    break
                else:
                    j +=1
                    count +=1
            if(found == False):
                result.append(0)
        return result
