// 209. Minimum Size Subarray Sum
// Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:

    // original
    // sliding window
    // not very efficient
    int minSubArrayLen(int target, vector<int>& nums) {
        int n = nums.size();
        int result = 0;
        int b = 0, e = 0;
        // sum of nums[b:e]
        int sum = 0;
        // keep nums[b:e] a window
        do {
            if (sum >= target) {
                result = result == 0 ? e - b : min(result, e - b);
                sum -= nums[b++];
            } else {
                ++e;
                if (e <= n) {
                    sum += nums[e - 1];
                }
            }
        } while (b < e && e <= n);
        return result;
    }

    // original
    // sliding window
    // not much improvement
    int minSubArrayLen2(int target, vector<int>& nums) {
        int n = nums.size();
        int result = n + 1;
        int sum = 0;
        int b = 0, e = -1;
        while (e < n) {
            if (sum >= target) {
                result = e - b + 1 < result ? e - b + 1 : result;
                sum -= nums[b++];
            } else {
                ++e;
                if (e < n) {
                    sum += nums[e];
                }
            }
        }
        return result == n + 1 ? 0 : result;
    }
};

int main() {

    Solution s;
    vector<int> v1{2,3,1,2,4,3};
    cout << s.minSubArrayLen2(7, v1) << endl; // 2
    vector<int> v2{1, 4, 4};
    cout << s.minSubArrayLen2(4, v2) << endl; // 1
    vector<int> v3{1,1,1,1,1,1,1,1};
    cout << s.minSubArrayLen2(11, v3) << endl; // 0
    vector<int> v4{1, 2, 3, 4, 5};
    cout << s.minSubArrayLen2(11, v4) << endl; // 3
}