class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        area = 0
        while(i < j):
            minimum = min(heights[i], heights[j])
            area = max(area, (j - i) * minimum)
            if(heights[i] < heights[j]):
                i += 1
            else:
                j -= 1
        return area
