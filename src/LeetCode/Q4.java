package LeetCode;

import java.util.Arrays;

/**
 * Didn't reach the advanced requirement, so it's not very efficient.
 */
public class Q4 {

    public static void main(String[] args) {
        int[] a = new int[]{1, 3};
        int[] b = new int[]{2};

        double result = findMedianSortedArrays(a, b);
        System.out.println(result);
    }

    public static double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] temp = combine(nums1, nums2);
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

    public static int[] combine(int[] array01, int[] array02) {
        int[] result = new int[array01.length + array02.length];
        System.arraycopy(array01, 0, result, 0, array01.length);
        System.arraycopy(array02, 0, result, array01.length, array02.length);
        return result;
    }

}
