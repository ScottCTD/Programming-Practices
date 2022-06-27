package LeetCode;

public class Q11 {

    public static void main(String[] args) {
        int result = maxArea02(new int[]{2, 3, 4, 5, 18, 17, 6});
        System.out.println(result);
    }

    // Almost original
    // Very efficient
    public static int maxArea02(int[] height) {
        int i = 0, j = height.length - 1, result = 0;

        while (i < j) {
            result = Math.max(result, Math.min(height[i], height[j]) * (j - i));
            if (height[i] > height[j]) {
                j--;
            } else {
                i++;
            }
        }

        return result;
    }

    // Original
    // Not efficient
    public static int maxArea01(int[] height) {
        int result = 0;
        for (int i = 0; i < height.length; i++) {
            for (int j = 0; j < height.length; j++) {
                if (i == j) continue;
                result = Math.max(result, (j - i) * Math.min(height[i], height[j]));
            }
        }
        return result;
    }

}
