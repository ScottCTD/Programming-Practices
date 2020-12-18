package LeetCode;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

/*
Very effective.
 */
public class Q1TwoSum {

    public static void main(String[] args) {
        System.out.println(Arrays.toString(twoSum02(new int[]{3, 2, 4}, 6)));
    }

    public static int[] twoSum01(int[] nums, int target) {
        int[] result = new int[2];
        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < nums.length; j++) {
                if (j == i) continue;
                if (nums[i] + nums[j] == target) {
                    result[0] = i;
                    result[1] = j;
                    return result;
                }
            }
        }
        return null;
    }

    // Map
    private static int[] twoSum02(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(target - nums[i])) {
                return new int[]{map.get(target - nums[i]), i};
            }
            map.put(nums[i], i);
        }
        return null;
    }

}
