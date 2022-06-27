package LeetCode;

import java.util.ArrayList;
import java.util.List;

/**
 * 01/16/2021 21:18
 * Need Review!!!
 * 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
 * n = 1
 * ()
 * n = 2
 * ()()
 * (())
 * n = 3
 * ()()()
 * ()(())
 * (())()
 * (()())
 * ((()))
 */
public class Q22 {

    public static void main(String[] args) {
        System.out.println(generateParenthesis01(2));
    }

    public static List<String> generateParenthesis01(int n) {
        List<String> result = new ArrayList<>();
        dfs(result, n, n, "");
        return result;
    }

    // Not original
    // Very effective
    // DFS
    private static void dfs(List<String> result, int left, int right, String temp) {
        if (left == 0 && right == 0) {
            result.add(temp);
            return;
        }
        if (left > 0) {
            dfs(result, left - 1, right, temp + '(');
        }
        if (right > left) {
            dfs(result, left, right - 1, temp + ')');
        }
    }

}
