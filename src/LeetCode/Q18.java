package LeetCode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * 给定一个包含n个整数的数组nums和一个目标值target，判断nums中是否存在四个元素 a，b，c和 d，使得a + b + c + d的值与target相等？
 * 找出所有满足条件且不重复的四元组。
 * 注意：
 * 答案中不可以包含重复的四元组。
 * 
 * 1, 0, -1, 0, -2, 2     0
 * -2,-1,-1,1,1,2,2       0
 */
public class Q18 {

    public static void main(String[] args) {
        System.out.println(fourSum(new int[]{-2, -1, -1, 1, 1, 2, 2}, 0));
    }

    // Almost Original - With a tiny tiny part got from others
    // Efficient - 7ms in LeetCode - Same idea as top method - Double index
    public static List<List<Integer>> fourSum(int[] nums, int target) {
        List<List<Integer>> result = new ArrayList<>();
        int length = nums.length;
        if (length < 4) return result;
        Arrays.sort(nums);
        if (nums[0] + nums[1] + nums[2] + nums[3] > target) return result;
        for (int i = 0; i < length; i++) {
            // Skip special
            if (i != 0 && nums[i] == nums[i - 1]) continue;
            if (nums[i] + nums[length - 1] + nums[length - 2] + nums[length - 3] < target) continue;
            for (int j = i + 1; j < length; j++) {
                if (j != i + 1 && nums[j] == nums[j - 1]) continue;
                if (nums[i] + nums[j] + nums[length - 1] + nums[length - 2] < target) continue;
                int left = j + 1, right = length - 1;
                while (left < right) {
                    int a = nums[i], b = nums[j], c = nums[left], d = nums[right], sum = a + b + c + d;
                    if (sum == target) {
                        result.add(Arrays.asList(a, b, c, d));
                        do {
                            left++;
                        } while (left < right && nums[left] == nums[left - 1]);
                        do {
                            right--;
                        } while (left < right && nums[right] == nums[right + 1]);
                    } else if (sum > target) {
                        right--;
                    } else {
                        left++;
                    }
                }
            }
        }
        return result;
    }

}
