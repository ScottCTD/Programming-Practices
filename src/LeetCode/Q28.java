package LeetCode;

/**
 * 实现strStr()函数。
 * <p>
 * 给定一个haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回 -1。
 */
public class Q28 {

    public static void main(String[] args) {
        System.out.println(strStr01("abc", "c"));
    }

    // Original
    // Efficient - 1ms in LeetCode - As same as the top method.
    public static int strStr01(String haystack, String needle) {
        if (needle.length() == 0) return 0;
        int needleLength = needle.length();
        for (int i = 0; i < haystack.length() - needleLength + 1; i++) {
            if (needle.equals(haystack.substring(i, i + needleLength))) {
                return i;
            }
        }
        return -1;
    }

}
