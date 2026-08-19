class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        total = m * n
        left = 0
        right = total - 1
        while(left <= right):
            mid = (left + right) // 2
            row = mid // n
            col = mid % n 
            val = matrix[row][col]

            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        return False