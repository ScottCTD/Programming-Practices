// 130. Surrounded Regions
// Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

// A region is captured by flipping all 'O's into 'X's in that surrounded region.

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    void solve(vector<vector<char>>& board) {
        int m = board.size(), n = board[0].size();
        for (int i = 0; i != m; ++i) {
            if (board[i][0] == 'O') dfs(board, m, n, i, 0);
        }
        for (int i = 0; i != m; ++i) {
            if (board[i][n - 1] == 'O') dfs(board, m, n, i, n - 1);
        }
        for (int i = 0; i != n; ++i) {
            if (board[0][i] == 'O') dfs(board, m, n, 0, i);
        }
        for (int i = 0; i != n; ++i) {
            if (board[m - 1][i] == 'O') dfs(board, m, n, m - 1, i);
        }
        for (int i = 0; i != m; ++i) {
            for (int j = 0; j != n; ++j) {
                if (board[i][j] == 'O') {
                    board[i][j] = 'X';
                }
            }
        }
        for (int i = 0; i != m; ++i) {
            for (int j = 0; j != n; ++j) {
                if (board[i][j] == 'A') {
                    board[i][j] = 'O';
                }
            }
        }
    }

    void dfs(vector<vector<char>>& board, int m, int n, int i, int j) {
        if (i == -1 || j == -1 || i == m || j == n || board[i][j] == 'X' || board[i][j] == 'A') {
            return;
        }
        board[i][j] = 'A';
        dfs(board, m, n, i, j + 1);
        dfs(board, m, n, i + 1, j);
        dfs(board, m, n, i, j - 1);
        dfs(board, m, n, i - 1, j);
    }
};

int main() {
    Solution s;

    vector<vector<char>> board1 = {{'X','O','X','O','X','O'},{'O','X','O','X','O','X'},{'X','O','X','O','X','O'},{'O','X','O','X','O','X'}};
    s.solve(board1);
}