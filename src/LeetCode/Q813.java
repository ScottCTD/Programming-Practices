package LeetCode;

/**
 * @author Scott_CTD
 * @create 2021/1/25 19:50
 *
 *         我们将给定的数组A分成K个相邻的非空子数组 ，我们的分数由每个子数组内的平均值的总和构成。计算我们所能得到的最大分数是多少。
 *
 *         注意我们必须使用 A 数组中的每一个数进行分组，并且分数不一定需要是整数。
 *
 *         9,1,2,3,9 3 1,2,3,4,5,6,7 4 4,1,7,5,6,2,3 4
 */
public class Q813 {

    public static void main(String[] args) {
        System.out.println(largestSumOfAverages01(new int[] { 9, 1, 2, 3, 9 }, 3));
    }

    // Original
    // Incomplete, need to learn more to do this kind of questions.
    public static double largestSumOfAverages01(int[] A, int K) {
        double result = 0;
        int length = A.length;
        int maxGroupLength = length - (K - 1);
        int currentGroups = 0;
        for (int i = 0; i < length; i++) {
            if (length - i <= K - currentGroups) {
                result += A[i];
                continue;
            }
            double average = 0;
            final int index = i;
            for (int j = 0; j < maxGroupLength; j++) {
                int sum = 0, k;
                for (k = 0; k <= j; k++) {
                    if (index + k >= length)
                        break;
                    sum += A[index + k];
                }
                double newAverage = sum / (j + 1D);
                if (newAverage > average) {
                    average = newAverage;
                    i = index + k - 1;
                }
            }
            result += average;
            currentGroups++;
        }
        return result;
    }

}