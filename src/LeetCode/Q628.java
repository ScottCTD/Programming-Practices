package LeetCode;

import java.util.Arrays;

/**
 * 给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
 * 1, 2, 3
 * 1, 2, 3, 4
 * -100,-98,-1,2,3,4
 * -1, -2, -3, -4
 */
public class Q628 {

    public static void main(String[] args) {
        System.out.println(maximumProduct(new int[]{-1, -2, -3, -4}));
    }

    public static int maximumProduct(int[] nums) {
        Arrays.sort(nums);
        int length = nums.length;
        return Math.max(nums[length - 1] * nums[0] * nums[1], nums[length - 1] * nums[length - 2] * nums[length - 3]);
    }

}
