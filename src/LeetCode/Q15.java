package LeetCode;

import java.util.*;

/**
 * 给你一个包含 n 个整数的数组nums，判断nums中是否存在三个元素 a，b，c ，使得a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
 * <p>
 * 注意：答案中不可以包含重复的三元组。
 * <p>
 * 等待继续完善
 * -1, 0, 1, 2, -1, -4
 * -4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0
 */
public class Q15 {

    public static void main(String[] args) {

        System.out.println(threeSum02(new int[]{-4, -2, 1, -5, -4, -4, 4, -2, 0, 4, 0, -2, 3, 1, -5, 0}));

    }

    // Original
    // Double Index
    // I don't know why this one is not efficient, it should be...
    private static List<List<Integer>> threeSum02(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        if (nums[0] >= 0) return result;
        for (int i = 0; i < nums.length; i++) {
            if (i != 0 && nums[i] == nums[i - 1]) continue;
            int j = i + 1, k = nums.length - 1;
            while (j < k) {
                int sum = nums[i] + nums[j] + nums[k];
                if (sum == 0) {
                    result.add(Arrays.asList(nums[i], nums[j], nums[k]));
                    do {
                        k--;
                    } while (j < k && nums[k] == nums[k + 1]);
                    do {
                        j++;
                    } while (j < k && nums[j] == nums[j - 1]);
                } else if (sum > 0) {
                    k--;
                } else {
                    j++;
                }
            }
        }
        return result;
    }

    // Original
    // Not efficient
    private static List<List<Integer>> threeSum01(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < nums.length && j != i; j++) {
                for (int k = 0; k < nums.length && k != i && k != j; k++) {
                    int a = nums[i], b = nums[j], c = nums[k];
                    if ((a + b + c) == 0) {
                        result.add(Arrays.asList(a, b, c));
                    }
                }
            }
        }

        return removeRepeated(result);
        //return result;
    }

    private static List<List<Integer>> removeRepeated(List<List<Integer>> target) {
        boolean[] isDeleted = new boolean[target.size()];
        int size = target.size();
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                if (j == i) continue;
                if (isDeleted[i] || isDeleted[j]) continue;
                List<Integer> a = target.get(i);
                List<Integer> b = target.get(j);
                if (equal(a, b)) {
                    isDeleted[j] = true;
                }
            }
        }
        for (int i = 0; i < isDeleted.length; i++) {
            if (isDeleted[i]) {
                target.set(i, null);
            }
        }
        target.removeIf(Objects::isNull);
        return target;
    }

    private static boolean equal(List<Integer> a, List<Integer> b) {
        Collections.sort(a);
        Collections.sort(b);
        if (b.equals(Arrays.asList(0, 0, 0))) {
            b = a;
            a = Arrays.asList(0, 0, 0);
        }
        for (Integer integer : b) {
            if (Collections.binarySearch(a, integer) < 0) {
                return false;
            }
        }
        return true;
    }

}
