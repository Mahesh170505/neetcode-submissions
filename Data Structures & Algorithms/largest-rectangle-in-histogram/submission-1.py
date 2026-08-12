class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        right_stack = []
        left_stack = []
        right_small = [0] * len(heights)
        left_small = [0] * len(heights)

        for i in range(len(heights) - 1, -1, -1):
            while right_stack and heights[i] <= right_stack[-1][0]:
                right_stack.pop()
            if not right_stack:
                right_small[i] = len(heights)
            else:
                right_small[i] = right_stack[-1][1]
            right_stack.append((heights[i], i))

        for i in range(len(heights)):
            while left_stack and heights[i] <= left_stack[-1][0]:
                left_stack.pop()
            if not left_stack:
                left_small[i] = -1
            else:
                left_small[i] = left_stack[-1][1]
            left_stack.append((heights[i], i))

        result = 0
        for i in range(len(heights)):
            width = right_small[i] - left_small[i] - 1
            area = heights[i] * width
            result = max(result, area)
        return result