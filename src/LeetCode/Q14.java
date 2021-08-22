package LeetCode;

/**
 * 编写一个函数来查找字符串数组中的最长公共前缀。
 * 
 * 如果不存在公共前缀，返回空字符串""。
 * 
 * 输入: ["flower","flow","flight"]
 * 输出: "fl"
 */
public class Q14 {

    public static void main(String[] args) {
        long time01 = System.currentTimeMillis();
        System.out.println(longestCommonPrefix(new String[]{"", ""}));
        long time02 = System.currentTimeMillis();
        System.out.println(time02 - time01);
    }

    // Original
    // Extremely efficient
    // Top Solution
    public static String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) return "";
        String result = strs[0];
        if (strs.length == 1) return strs[0];
        for (int i = 0; i < strs.length; i++) {
            if (!strs[i].startsWith(result)) {
                result = result.substring(0, result.length() - 1);
                i--;
            }
        }

        return result;
    }

}
