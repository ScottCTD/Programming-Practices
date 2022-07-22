package LeetCode;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

/*
Very efficient.
 */
public class Q1TwoSum {

    public static void main(String[] args) {
        System.out.println(Arrays.toString(twoSum02(new int[] { 3, 2, 4 }, 6)));
    }

    /*
     * Original Very efficient My personal solutions in Java and C, using a very
     * direct way of double for loops.
     */
    public static int[] twoSum01(int[] nums, int target) {
        int[] result = new int[2];
        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < nums.length; j++) {
                if (j == i)
                    continue;
                if (nums[i] + nums[j] == target) {
                    result[0] = i;
                    result[1] = j;
                    return result;
                }
            }
        }
        return null;
    }

    /*
     * Map 这个方法用一个Map来存储数组当中的key和value的，这里为了方便，把数组内的value设置为map的key，而index为value。
     * 这个时候，如果这个map里面有target -
     * nums[i]对应的value，就代表这俩map中的value是答案，然后每一次循环都把这个循环的东西放进去。时间复杂度为O(n)。
     * 同时，这个方法也满足不重复用数的规则。
     */
    private static int[] twoSum02(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(target - nums[i])) {
                return new int[] { map.get(target - nums[i]), i };
            }
            map.put(nums[i], i);
        }
        return null;
    }

}
