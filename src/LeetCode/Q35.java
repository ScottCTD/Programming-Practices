package LeetCode;

/**
 * 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
 * <p>
 * 你可以假设数组中无重复元素。
 * <p>
 * 1,3,5,6 5
 */
public class Q35 {

    public static void main(String[] args) {
        System.out.println(searchInsert01(new int[]{1, 3, 5, 6, 9, 120000}, 100));
    }

    // Original
    // 0 ms in LeetCode - Top Method - Binary Search
    public static int searchInsert01(int[] nums, int target) {
        if (nums.length == 1) return nums[0] < target ? 1 : 0;
        int left = 0, right = nums.length - 1, middle = 0;
        while (left <= right) {
            middle = (left + right) >>> 1;
            int value = nums[middle];
            if (value > target) {
                right--;
            } else if (value < target) {
                left++;
            } else {
                return middle;
            }
        }
        return middle == right ? middle + 1 : middle;
    }

}
