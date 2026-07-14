class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = []
        for i in range(len(temperatures)):
            result.append(0)
        
        for i in range(len(temperatures) - 1, -1, -1):
            while(stack and temperatures[i] >= stack[-1][0]):
                stack.pop()
            if(stack and temperatures[i] < stack[-1][0]):
                days = stack[-1][1] - i
                result[i] = days
            stack.append((temperatures[i], i))
        return result