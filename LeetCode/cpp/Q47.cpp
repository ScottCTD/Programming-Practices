// 47. Permutations II
// Given a collection of numbers, nums, that might contain duplicates, return
// all possible unique permutations in any order.

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    // half-original
    // learned how to eliminate duplicates
    vector<vector<int>> permuteUnique(vector<int> &nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> result;
        vector<int> perm;
        vector<bool> used(nums.size(), false);
        func(nums, result, used, perm);
        return result;
    }

    void func(vector<int> &nums, vector<vector<int>> &result, vector<bool> &used, vector<int> &perm) {
        int n = nums.size();
        if (perm.size() == n) {
            result.push_back(perm);
            return;
        }
        for (int j = 0; j != n; ++j) {
            int num = nums[j];
            // learned
            if (j != 0 && num == nums[j - 1] && used[j - 1]) {
                continue;
            }
            if (!used[j]) {
                perm.push_back(num);
                used[j] = true;
                func(nums, result, used, perm);
                perm.pop_back();
                used[j] = false;
            }
        }
    }
};

int main() {
    Solution s;

    vector<int> nums = {1, 2, 3};
    s.permuteUnique(nums);

    vector<int> nums2 = {1, 1, 2};
    s.permuteUnique(nums2);
}