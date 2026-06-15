class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashmap: List[List[bool]] = [[False for _ in range(9)] for _ in range(27)]

        for i in range(9):  
            for j in range(9):
                value = board[i][j]

                if value == ".": continue

                value = ord(value) - 49
                box = ((i // 3) * 3) + (j // 3)
                
                if hashmap[i][value] or hashmap[j+9][value] or hashmap[box+18][value]: 
                    return False
                
                hashmap[i][value] = True
                hashmap[j+9][value] = True
                hashmap[box+18][value] = True
        
        return True