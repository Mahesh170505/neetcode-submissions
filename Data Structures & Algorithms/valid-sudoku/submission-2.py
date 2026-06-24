from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        
        for row in range(9):
            seen = set()
            for col in range(9):
                val = board[row][col]
                
                if val == ".":
                    continue
                
                if val in seen:
                    return False
                
                seen.add(val)
        
        
        for col in range(9):
            seen = set()
            for row in range(9):
                val = board[row][col]
                
                if val == ".":
                    continue
                
                if val in seen:
                    return False
                
                seen.add(val)

        
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j

                    val = board[row][col]

                    if val == ".":
                        continue
                    
                    if val in seen:
                        return False
                    
                    seen.add(val)
        
        return True
