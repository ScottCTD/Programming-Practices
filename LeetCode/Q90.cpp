// 90. Subsets II
// Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

// The solution set must not contain duplicate subsets. Return the solution in any order.

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:

    // original
    // backtrack
    // time efficient but memory inefficient
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> result;
        func(nums, 0, result);
        return result;
    }

    int func(vector<int>& nums, const int &i, vector<vector<int>> &result) {
        int n = nums.size();
        if (i == n) {
            result.push_back({});
            return 1;
        }
        int delta = func(nums, i + 1, result);
        int size = result.size();
        if (i == n - 1 || nums[i] != nums[i + 1]) {
            for (int j = 0; j != size; ++j) {
                auto u = result[j];
                vector<int> v = {nums[i]};
                v.insert(v.cend(), u.cbegin(), u.cend());
                result.push_back(v);
            }
            return size;
        } else {
            for (int j = size - delta; j != size; ++j) {
                auto u = result[j];
                vector<int> v = {nums[i]};
                v.insert(v.cend(), u.cbegin(), u.cend());
                result.push_back(v);
            }
            return delta;
        }
        
    }

};