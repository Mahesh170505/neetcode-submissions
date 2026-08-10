class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures) - 1, -1, -1):
            while (stack and temperatures[i] >= stack[-1][0]):
                stack.pop()
            if not stack:
                result[i] = 0
            else:
                result[i] = stack[-1][1] - i
            stack.append((temperatures[i], i))
        return result