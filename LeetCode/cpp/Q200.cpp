// 200. Number of Islands
// Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

// An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:

    // original
    // recurse into every '1' and mark it is occupied ('2')
    int numIslands(vector<vector<char>>& grid) {
        int row = grid.size(), column = grid[0].size();
        int result = 0;
        for (int i = 0; i != row; ++i) {
            for (int j = 0; j != column; ++j) {
                if (grid[i][j] == '1') {
                    func(grid, i, j);
                    ++result;
                }
            }
        }
        return result;
    }

    void func(vector<vector<char>>& grid, int row, int column) {
        if (row == -1 || row == grid.size() ||
            column == -1 || column == grid[0].size() || 
            grid[row][column] != '1') {
                return;
            }
        grid[row][column] = '2';
        // clock-wise rotate
        func(grid, row, column + 1);
        func(grid, row + 1, column);
        func(grid, row, column - 1);
        func(grid, row - 1, column);
    }
};