class Solution:
    def trap(self, height: List[int]) -> int:
        left_height = 0
        right_height = 0
        total_height = 0

        for a in range(len(height)):
            prefix_height = 0
            while(prefix_height <= a):
                left_height = max(height[prefix_height],left_height)
                prefix_height += 1  
            suffix_height = len(height) - 1
            while(suffix_height >= a):
                right_height = max(height[suffix_height],right_height)
                suffix_height -= 1
            total_height += min(left_height, right_height) - height[a]
            left_height = 0
            right_height = 0

        return total_height