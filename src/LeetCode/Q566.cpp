/**
 * 2021/02/17
 * 在MATLAB中，有一个非常有用的函数 reshape，它可以将一个矩阵重塑为另一个大小不同的新矩阵，但保留其原始数据。
 * 给出一个由二维数组表示的矩阵，以及两个正整数r和c，分别表示想要的重构的矩阵的行数和列数。
 * 重构后的矩阵需要将原始矩阵的所有元素以相同的行遍历顺序填充。
 * 如果具有给定参数的reshape操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。
 */

#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    
    // Original
    // Relatively Not Very Efficient - 18 ms in LeetCode
    vector<vector<int>> matrixReshape01(vector<vector<int>> &nums, int r, int c) {
        if (nums.size() * nums.at(0).size() != r * c) {
            return nums;
        }
        vector<vector<int>> *result = new vector<vector<int>>();
        result->resize(r);
        int index = 0;
        int subIndex = 0;
        for (vector<vector<int>>::const_iterator iterator = nums.begin(); iterator != nums.end(); ++iterator) {
            for (vector<int>::const_iterator subIterator = (*iterator).begin(); subIterator != (*iterator).end(); ++subIterator) {
                if (subIndex >= c) {
                    ++index;
                    subIndex = 0;
                }
                if (result->size() <= index) {
                    result->push_back(*(new vector<int>));
                    result->at(index).resize(c);
                }
                result->at(index).push_back(*subIterator);
                ++subIndex;
            }
        }
        return *result;
    }

    // Original
    // Efficient -> 12 ms in LeetCode
    vector<vector<int>> matrixReshape02(vector<vector<int>> &nums, int r, int c) {
        int realRow = nums.size(), realColumn = nums[0].size();
        if (realRow * realColumn != r * c) {    
            return nums;
        }
        vector<vector<int>> result (r, vector<int> (c, 0));
        int index = 0, subIndex = 0;
        for (int i = 0; i < realRow; ++i) {
            for (int j = 0; j < realColumn; ++j) {
                if (subIndex >= c) {
                    ++index;
                    subIndex = 0;
                }
                result[index][subIndex] = nums[i][j];
                ++subIndex;
            }
        }
        return result;
    }

};

int main() {
    vector<vector<int>> *nums = new vector<vector<int>>();
    vector<int> *v01 = new vector<int>;
    v01->push_back(1);
    v01->push_back(2);
    vector<int> *v02 = new vector<int>;
    v02->push_back(3);
    v02->push_back(4);
    nums->push_back(*v01);
    nums->push_back(*v02);

    vector<vector<int>> result = Solution ().matrixReshape02(*nums, 1, 4);

    for (vector<vector<int>>::const_iterator iterator = result.begin(); iterator != result.end(); ++iterator) {
        for (vector<int>::const_iterator subIterator = (*iterator).begin(); subIterator != (*iterator).end(); ++subIterator) {
            cout << *subIterator << " " << endl;
        }
        cout << endl;
    }

    delete nums;
    delete v01;
    delete v02;
    return 0;
}