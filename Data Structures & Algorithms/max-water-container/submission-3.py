class Solution:
    def maxArea(self, heights: List[int]) -> int:
        curr_area = 0
        final_area = 0
        i = 0
        j = len(heights) - 1
        
        while(i < j):
            curr_area = min(heights[i], heights[j]) * (j - i)
            final_area = max(final_area, curr_area)
            if(heights[i] < heights[j]):
                i += 1
            else:
                j -= 1
            
            
        return final_area
