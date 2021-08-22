package LeetCode;

/**
 * 判断一个9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。
 * 
 * 数字1-9在每一行只能出现一次。
 * 数字1-9在每一列只能出现一次。
 * 数字1-9在每一个以粗实线分隔的3x3宫内只能出现一次。
 */
public class Q36 {

    public static void main(String[] args) {
        char[][] board = {
                {'5', '3', '.', '.', '7', '.', '.', '.', '.'},
                {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
                {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
                {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
                {'4', '.', '.', '8', '.', '3', '.', '.', '1'},
                {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
                {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
                {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
                {'.', '.', '.', '.', '8', '.', '.', '7', '9'}
        };
        System.out.println(isValidSudoku(board));
    }

    // Original
    // 2 ms in LeetCode - Nearly the Top method
    // Just iterate and control flow
    public static boolean isValidSudoku(char[][] board) {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.') continue;
                char value = board[i][j];
                // Row
                for (int k = 0; k < 9; k++) {
                    if (board[i][k] == value && k != j) {
                        return false;
                    }
                }
                // Column
                for (int k = 0; k < 9; k++) {
                    if (board[k][j] == value && k != i) {
                        return false;
                    }
                }
                // 3 * 3
                int boxRow = i / 3, boxColumn = j / 3;
                for (int k = 0; k < 3; k++) {
                    int realRow = boxRow * 3 + k;
                    for (int l = 0; l < 3; l++) {
                        int realColumn = boxColumn * 3 + l;
                        if (board[realRow][realColumn] == value) {
                            if (realRow == i && realColumn == j) continue;
                            return false;
                        }
                    }
                }
            }
        }
        return true;
    }

}
