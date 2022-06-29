// 1091. Shortest Path in Binary Matrix
// Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

// A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

// All the visited cells of the path are 0.
// All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
// The length of a clear path is the number of visited cells of this path.

#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:

    // original depth first search
    // correct but not efficient and messy
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        int n = grid.size();
        if (grid[0][0] != 0 || grid[n - 1][n - 1] != 0) {
            return -1;
        }
        int result = func(grid, n, 0, 0);
        return result == 0 ? -1 : result;
    }

    int func(vector<vector<int>>& grid, int n, int i, int j) {
        if (i == -1 || j == -1 || i == n || j == n || grid[i][j] == 1 || grid[i][j] == -1) {
            return 0;
        }
        if (i == n - 1 && j == n - 1) {
            return 1;
        }
        grid[i][j] = -1;
        vector<int> lens = {
            func(grid, n, i, j + 1),
            func(grid, n, i + 1, j + 1),
            func(grid, n, i + 1, j),
            func(grid, n, i + 1, j - 1),
            func(grid, n, i, j - 1),
            func(grid, n, i - 1, j - 1),
            func(grid, n, i - 1, j),
            func(grid, n, i - 1, j + 1)
        };
        int min_length = -1;
        for (int len : lens) {
            if (len != 0) {
                if (min_length == -1) {
                    min_length = len;
                } else {
                    min_length = min(min_length, len);
                }
            }
        }
        grid[i][j] = 0;
        return min_length + 1;
    }
};

class Solution2 {
public:

    vector<pair<int, int>> directions = {{0, 1}, {1, 1}, {1, 0}, {1, -1}, {0, -1}, {-1, -1}, {-1, 0}, {-1, 1}};

    // learned (half original)
    // learned breadth first search
    // search level by level
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        int n = grid.size();
        if (grid[0][0] == 1 || grid[n - 1][n - 1] == 1) {
            return -1;
        }
        int result = 1;
        queue<pair<int, int>> q;
        q.emplace(0, 0);
        grid[0][0] = 1;
        while (!q.empty()) {
            int size = q.size();
            // handle the entire layer
            for (int _ = 0; _ != size; ++_) {
                auto curr = q.front();
                if (curr.first == n - 1 && curr.second == n - 1) {
                    return result;
                }
                q.pop();
                // search for the next layer
                for (auto dir : this->directions) {
                    int i = curr.first + dir.first, j = curr.second + dir.second;
                    if (i != -1 && j != -1 && i != n && j != n && grid[i][j] == 0) {
                        q.emplace(i, j);
                        grid[i][j] = 1;
                    }
                }
            }
            ++result;
        }
        return -1;
    }
};

int main() {
    Solution s;
    Solution2 s2;

    vector<vector<int>> grid1 = {{0, 1}, {1, 0}};
    cout << s.shortestPathBinaryMatrix(grid1) << endl;
    cout << s2.shortestPathBinaryMatrix(grid1) << endl;

    vector<vector<int>> grid2 = {{0, 0, 1, 0}, {1, 0, 1, 0}, {1, 1, 0, 1}, {0, 0, 0, 0}};
    cout << s.shortestPathBinaryMatrix(grid2) << endl;
    cout << s2.shortestPathBinaryMatrix(grid2) << endl;

    // [[0,1,1,0,0,0],[0,1,0,1,1,0],[0,1,1,0,1,0],[0,0,0,1,1,0],[1,1,1,1,1,0],[1,1,1,1,1,0]]
    vector<vector<int>> grid3 = {{0,1,1,0,0,0},{0,1,0,1,1,0},{0,1,1,0,1,0},{0,0,0,1,1,0},{1,1,1,1,1,0},{1,1,1,1,1,0}};
    cout << s.shortestPathBinaryMatrix(grid3) << endl;
    cout << s2.shortestPathBinaryMatrix(grid3) << endl;
}