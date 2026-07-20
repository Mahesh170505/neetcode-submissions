class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        right_stack = []
        right_array = [n] * n

        left_stack = []
        left_array = [-1] * n

        result = 0

        
        for i in range(n - 1, -1, -1):
            while (
                right_stack
                and heights[right_stack[-1]] >= heights[i]
            ):
                right_stack.pop()

            if right_stack:
                right_array[i] = right_stack[-1]

            right_stack.append(i)

        
        for i in range(n):
            while (
                left_stack
                and heights[left_stack[-1]] >= heights[i]
            ):
                left_stack.pop()

            if left_stack:
                left_array[i] = left_stack[-1]

            left_stack.append(i)

        
        for i in range(n):
            width = right_array[i] - left_array[i] - 1
            current_area = heights[i] * width
            result = max(result, current_area)

        return result