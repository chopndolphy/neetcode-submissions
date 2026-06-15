class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) { 

    // 243 bits packed tightly into 31 bytes
    uint8_t state[31] = {0}; 

    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            char val = board[i][j];
            if (val == '.') continue;

            int num = val - '1'; // 0 to 8
            int box = (i / 3) * 3 + (j / 3);

            // Calculate the absolute bit positions (0 to 242)
            int row_bit = (0 * 81) + (i * 9) + num;
            int col_bit = (1 * 81) + (j * 9) + num;
            int box_bit = (2 * 81) + (box * 9) + num;

            // Check and set for Row
            if ((state[row_bit / 8] & (1 << (row_bit % 8)))) return false;
            state[row_bit / 8] |= (1 << (row_bit % 8));

            // Check and set for Column
            if ((state[col_bit / 8] & (1 << (col_bit % 8)))) return false;
            state[col_bit / 8] |= (1 << (col_bit % 8));

            // Check and set for Box
            if ((state[box_bit / 8] & (1 << (box_bit % 8)))) return false;
            state[box_bit / 8] |= (1 << (box_bit % 8));
        }
    }
    return true;
}

};