class Solution:
    def trap(self, height: List[int]) -> int:
        left_values = [0] * len(height)
        right_values = [0] * len(height)
        left_values[0] = height[0]
        right_values[len(height) - 1] = height[len(height) - 1]
        total_height = 0

        for i in range(1, len(height)):
            left_values[i] = max(left_values[i - 1], height[i])
        for i in range(len(height)- 2, -1, -1):
            right_values[i] = max(right_values[i + 1], height[i])
        for i in range(len(height)):
            total_height += min(left_values[i], right_values[i]) - height[i]
        return total_height
