class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                
                if val == '.':
                    continue
                    
                # Create unique signatures for each constraint
                row_sig = (val, "row", i)
                col_sig = (val, "col", j)
                box_sig = (val, "box", i // 3, j // 3)
                
                # If we've already seen this exact number in this scope, it's invalid
                if row_sig in seen or col_sig in seen or box_sig in seen:
                    return False
                    
                # Add our tracking signatures
                seen.add(row_sig)
                seen.add(col_sig)
                seen.add(box_sig)
                
        return True
 