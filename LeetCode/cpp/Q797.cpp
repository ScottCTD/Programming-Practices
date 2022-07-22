// 797. All Paths From Source to Target
// Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

// The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        vector<vector<int>> result;
        dfs(graph, graph.size(), 0, result, {0});
        return result;
    }

    void dfs(vector<vector<int>>& graph, const int n, const int i,
             vector<vector<int>> &result, vector<int> path) {
        if (i == n - 1) {
            result.push_back(path);
            return;
        }
        for (int j : graph[i]) {
            path.push_back(j);
            dfs(graph, n, j, result, path);
            path.pop_back();
        }
    }
};

void print_vector(vector<vector<int>> result) {
    cout << "[";
    for (const auto& i : result) {
        cout << "[";
        for (auto j : i) {
            cout << j << ", ";
        }
        cout << "], ";
    }
}

int main() {
    Solution s;
    vector<vector<int>> graph1 = {{1,2}, {3}, {3}, {}};
    print_vector(s.allPathsSourceTarget(graph1));
}