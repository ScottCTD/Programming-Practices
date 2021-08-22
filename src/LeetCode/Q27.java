package LeetCode;

import java.util.Arrays;

/**
 * 01/16/2021 23:01
 * 
 * 给你一个数组 nums和一个值 val，你需要 原地 移除所有数值等于val的元素，并返回移除后数组的新长度。
 * 
 * 不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
 * 
 * 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
 * 
 * 3,2,2,3 0,1,2,2,3,0,4,2
 */
public class Q27 {

    public static void main(String[] args) {
        int[] nums = { 0, 1, 2, 2, 3, 0, 4, 2 };
        System.out.println(removeElement01(nums, 2) + "   " + Arrays.toString(nums));
    }

    // Original
    // Efficient - 0ms in LeetCode - Top Method
    public static int removeElement01(int[] nums, int val) {
        int i = 0;
        for (int j = 0; j < nums.length; j++) {
            if (nums[j] != val) {
                nums[i++] = nums[j];
            }
        }
        return i;
    }

}
