package LeetCode;

import xyz.scottc.scu.ArrayUtils;

import java.util.Arrays;

/**
 * Didn't reach the advanced requirement, so it's not very effective.
 */
public class Q4 {

    public static void main(String[] args) {
        int[] a = new int[]{1, 3};
        int[] b = new int[]{2};

        double result = findMedianSortedArrays(a, b);
        System.out.println(result);
    }

    public static double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] temp = ArrayUtils.combine(nums1, nums2);
        if (temp.length == 0) return 0;
        if (temp.length == 1) return temp[0];

        Arrays.sort(temp);

        if (temp.length % 2 != 0) {
            return temp[(temp.length / 2)];
        } else {
            int index = temp.length / 2 - 1;
            return (temp[index] + temp[index + 1]) / 2D;
        }
    }

}
