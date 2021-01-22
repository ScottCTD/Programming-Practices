package LeetCode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * 给定一个无重复元素的数组candidates和一个目标数target，找出candidates中所有可以使数字和为target的组合。
 * candidates中的数字可以无限制重复被选取。
 * <p>
 * 说明：
 * 所有数字（包括target）都是正整数。
 * 解集不能包含重复的组合。
 * <p>
 * 2,3,6,7 7
 * 2, 3, 5 8
 * <p>
 * 回溯算法，暂时不做
 */
public class Q39 {

    public static void main(String[] args) {
        System.out.println(combinationSum(new int[]{2, 3, 5}, 8));
    }

    public static List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<List<Integer>> result = new ArrayList<>();
        int length = candidates.length;
        for (int i = 0; i < length; i++) {
            List<Integer> temp = new ArrayList<>();
            int sum = candidates[i], index = i;
            temp.add(candidates[i]);
            while (sum != target) {
                if (result.size() != 0) {

                }
            }
            if (sum == target) {
                result.add(temp);
            }
        }
        return result;
    }

}
