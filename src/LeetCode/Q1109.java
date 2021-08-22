package LeetCode;

import java.util.Arrays;

/**
 * 这里有n个航班，它们分别从 1 到 n 进行编号。
 * 
 * 我们这儿有一份航班预订表，表中第i条预订记录bookings[i] = [j, k, l]意味着我们在从 j到 k的每个航班上预订了 l个座位。
 * 
 * 请你返回一个长度为 n 的数组answer，按航班编号顺序返回每个航班上预订的座位数
 * 
 * 等待继续完善
 */
public class Q1109 {

    public static void main(String[] args) {
        System.out.println(
                Arrays.toString(corpFlightBookings(new int[][] { { 1, 2, 10 }, { 2, 3, 20 }, { 2, 5, 25 } }, 5)));
    }

    // Original
    // Not Effective
    public static int[] corpFlightBookings(int[][] bookings, int n) {
        int[] result = new int[n];
        for (int i = 0; i < bookings.length; i++) {
            int start = bookings[i][0];
            int diff = bookings[i][1] - start;
            for (int j = start; j <= start + diff; j++) {
                result[j - 1] += bookings[i][2];
            }
        }
        return result;
    }

}
