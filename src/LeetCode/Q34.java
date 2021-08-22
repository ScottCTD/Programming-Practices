package LeetCode;

import java.util.Arrays;

/**
 * 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。 如果数组中不存在目标值
 * target，返回[-1, -1]。 进阶： 你可以设计并实现时间复杂度为O(log n)的算法解决此问题吗？ 5,7,7,8,8,10 8 1 1
 */
public class Q34 {

    public static void main(String[] args) {
        System.out.println(Arrays.toString(searchRange02(new int[] { 5, 7, 7, 8, 8, 10 }, 6)));
    }

    // 01/20/2021 00:04
    // Original
    // 0 ms in LeetCode - Top Method
    // Use binary search to get the pos of target, then spread left and right index
    // to find the bound of target number.
    public static int[] searchRange02(int[] nums, int target) {
        int length = nums.length;
        int left = 0, right = nums.length - 1;
        int mid = 0;
        boolean found = false;
        while (left <= right) {
            mid = (left + right) >>> 1;
            int value = nums[mid];
            if (value < target) {
                left = mid + 1;
            } else if (value > target) {
                right = mid - 1;
            } else {
                found = true;
                break;
            }
        }
        if (!found)
            return new int[] { -1, -1 };
        left = right = mid;
        while (left >= 0 && nums[left] == target) {
            left--;
        }
        while (right < length && nums[right] == target) {
            right++;
        }
        return new int[] { left + 1, right - 1 };
    }

    // 01/19/2021 09:00
    // Original
    // Not very efficient comparatively - 1 ms in LeetCode
    // Double Index (No!!
    public static int[] searchRange01(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        while (left <= right) {
            if (nums[left] == target && nums[right] == target) {
                return new int[] { left, right };
            }
            if (nums[left] == target) {
                right--;
                continue;
            }
            if (nums[right] == target) {
                left++;
                continue;
            }
            left++;
            right--;
        }
        return new int[] { -1, -1 };
    }

}
