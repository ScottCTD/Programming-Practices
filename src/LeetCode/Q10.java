package LeetCode;

/**
 * 给你一个字符串s和一个字符规律p，请你来实现一个支持 '.'和'*'的正则表达式匹配。
 * <p>
 * '.' 匹配任意单个字符
 * '*' 匹配零个或多个前面的那一个元素
 * 所谓匹配，是要涵盖整个字符串s的，而不是部分字符串。
 * <p>
 * 暂时没解决
 */
public class Q10 {

    public static void main(String[] args) {

    }

    public boolean isMatch(String s, String p) {
        if (p.isEmpty() && !s.isEmpty()) return false;
        if (p.isEmpty()) return true;
        if (p.equals(".*")) return true;
        if (!p.contains(".") && !p.contains("*") && !s.equals(p)) return false;


        return false;
    }

}
