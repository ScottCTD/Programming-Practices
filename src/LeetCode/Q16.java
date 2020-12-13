package LeetCode;

import java.util.Arrays;

/**
 * 给定一个包括n 个整数的数组nums和 一个目标值target。找出nums中的三个整数，使得它们的和与target最接近。返回这三个数的和。假定每组输入只存在唯一答案。
 * 输入：nums = [-1,2,1,-4], target = 1
 * 输出：2
 * 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
 */
public class Q16 {

    public static void main(String[] args) {
        int i = threeSumClosest02(new int[]{3, 4, 5, 5, 7}, 13);
        System.out.println(i);
    }

    // Learned
    // Very effective
    // 双指针
    private static int threeSumClosest02(int[] nums, int target) {
        Arrays.sort(nums);
        int result = nums[0] + nums[1] + nums[2];
        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            int j = i + 1, k = nums.length - 1;
            while (j < k) {
                int sum = nums[i] + nums[j] + nums[k];
                if (Math.abs(result - target) > Math.abs(sum - target)) {
                    result = sum;
                }
                // 数组这个时候左边是小的，右边是大的
                // 如果现在的sum比target大，那就往小里找
                if (sum > target) {
                    do {
                        k--;
                    } while (k > j && nums[k] == nums[k + 1]);
                } else if (sum < target) { // 如果这个时候sum比target小，说明这个sum太小了，就往大里找
                    do {
                        j++;
                    } while (j < k && nums[j] == nums[j - 1]);
                } else { //如果这个时候sum等于target了，他俩的区别就是0了，就是最接近了
                    return sum;
                }
            }
        }
        return result;
    }

    // Original
    // Not effective
    private static int threeSumClosest01(int[] nums, int target) {
        int result = 0;
        Arrays.sort(nums);
        for (int i = 0; i < nums.length; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            for (int j = i + 1; j < nums.length; j++) {
                if (j > i + 1 && nums[j] == nums[j - 1]) continue;
                for (int k = j + 1; k < nums.length; k++) {
                    if (k > j + 1 && nums[k] == nums[k - 1]) continue;
                    int a = nums[i], b = nums[j], c = nums[k], sum = a + b + c;
                    int diff01 = Math.abs(result - target), diff02 = Math.abs(sum - target);
                    if (diff02 == 0) return sum;
                    if (k == 2) result = sum;
                    if (k != 2 && diff01 > diff02) result = sum;
                }
            }
        }
        return result;
    }

}
