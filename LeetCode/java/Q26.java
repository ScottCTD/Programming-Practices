package LeetCode;

import java.util.Arrays;

/**
 * 01/16/2021 21:19
 * 给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
 * 
 * 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
 * 
 * 1, 2, 3
 * 1,1,2
 * 0,0,1,1,1,2,2,3,3,4
 * 1, 2, 2
 * 1,1,2,3
 */
public class Q26 {

    public static void main(String[] args) {
        int[] test = {1, 1, 2};
        int result = removeDuplicates01(test);
        System.out.println(Arrays.toString(test) + "    " + result);
    }

    // Not Original
    // Same idea as mine but cleaner
    public static int removeDuplicates02(int[] nums) {
        int i = 0;
        for (int j = 1; j < nums.length; j++) {
            if (nums[j] != nums[i]) {
                nums[++i] = nums[j];
            }
        }
        return i + 1;
    }


    // Original
    // Efficient 1ms in LeetCode
    public static int removeDuplicates01(int[] nums) {
        int index = 0;
        for (int i = 0; i < nums.length; i++) {
            int j = i + 1;
            while (j < nums.length) {
                if (nums[i] != nums[j]) break;
                j++;
            }
            if (j >= nums.length) {
                return index + 1;
            }
            nums[++index] = nums[j];
            if (i + 1 != j) i = j - 1;
        }
        return index + 1;
    }

}
