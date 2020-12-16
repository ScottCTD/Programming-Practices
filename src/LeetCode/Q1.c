#include <stdio.h>
#include <stdlib.h>

/*
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
*/

int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    for (int i = 0; i < numsSize; ++i) {
        for (int j = i + 1; j < numsSize; ++j) {
            if (nums[i] + nums[j] == target) {
                int* result = malloc(sizeof(int) * 2);
                result[0] = i, result[1] = j;
                *returnSize = 2;
                return result;
            }
        }
    }
    *returnSize = 0;
    return NULL;
}

int main() {
    int nums[] = {2, 7, 11, 15};
    int target = 9;

    int* result;
    int returnSize;

    result = twoSum(nums, sizeof(nums) / sizeof(nums[0]), target, &returnSize);

    //printf("%d, %d", result[0], result[1]);

    for (int i = 0; i < returnSize; ++i) {
        printf("%d ", result[i]);
    }

    return 0;
}