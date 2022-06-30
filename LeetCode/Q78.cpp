// 78. Subsets
// Given an integer array nums of unique elements, return all possible subsets (the power set).

// The solution set must not contain duplicate subsets. Return the solution in any order.

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> result;
        result.reserve(n - 1);
        func(nums, n, 0, result);
        return result;
    }

    void func(vector<int>& nums, const int &n, const int &i, vector<vector<int>> &result) {
        if (i == n) {
            result.push_back({});
            return;
        }
        func(nums, n, i + 1, result);
        int size = result.size();
        for (int j = 0; j != size; ++j) {
            auto u = result[j];
            vector<int> v = {nums[i]};
            v.insert(v.cend(), u.cbegin(), u.cend());
            result.push_back(v);
        }
    }

};