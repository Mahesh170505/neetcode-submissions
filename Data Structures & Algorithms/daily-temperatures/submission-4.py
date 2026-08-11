class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures) - 1, - 1, - 1):
            while stack and temperatures[i] >= stack[-1][0]:
                stack.pop()
            if(not stack):
                stack.append((temperatures[i], i))
                result[i] = 0
            else:
                days = stack[-1][1] - i
                result[i] = days
                stack.append((temperatures[i], i))
        return result
            