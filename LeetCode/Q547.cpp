// 547. Number of Provinces
// There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

// A province is a group of directly or indirectly connected cities and no other cities outside of the group.

// You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

// Return the total number of provinces.

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:

    // original
    // not very efficient
    // idea of deep first search
    int findCircleNum(vector<vector<int>>& isConnected) {
        int n = isConnected.size();
        int result = 0;
        for (int i = 0; i != n; ++i) {
            for (int j = 0; j != n; ++j) {
                if (isConnected[i][j] == 1) {
                    func(isConnected, n, i, j);
                    ++result;
                }
            }
        }
        return result;
    }

    void func(vector<vector<int>>& isConnected, int n, int i, int j) {
        isConnected[i][j] = 2;
        isConnected[j][i] = 2;
        isConnected[i][i] = 2;
        isConnected[j][j] = 2;

        for (int col = 0; col != n; ++col) {
            if (isConnected[i][col] == 1) {
                func(isConnected, n, i, col);
            }
        }
        for (int row = 0; row != n; ++row) {
            if (isConnected[row][j] == 1) {
                func(isConnected, n, row, j);
            }
        }
    }
};

int main() {
    Solution s1;
    
    vector<vector<int>> v = {{1, 1, 0}, {1, 1, 0}, {0, 0, 1}};
    cout << s1.findCircleNum(v) << endl;
}