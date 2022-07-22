package LeetCode;

public class Q8 {

    public static void main(String[] args) {

        System.out.println(myAtoi02("0000000000012345678"));
    }

    // Original - 12/23/2020 20:27
    // Relatively efficient - 5 ms in leetcode
    // Important change: no Integer.parse() anymore!
    // (char - '0') should equal to it's real digit
    private static int myAtoi02(String s) {
        if (s.isBlank()) return 0;
        s = s.trim();

        char first = s.charAt(0);
        boolean sign = true; // true -> + | false -> -
        long result = 0;
        if (first == '-') {
            sign = false;
        } else if (isDigit(first)) {
            result = first - '0';
        } else if (first != '+') {
            return 0;
        }

        for (int i = 1; i < s.length(); i++) {
            char c = s.charAt(i);
            if (!isDigit(c)) break;
            result = result * 10 + (c - '0');
            if (i > 8) {
                if (sign) {
                    if (result > Integer.MAX_VALUE) return Integer.MAX_VALUE;
                } else {
                    if (-result < Integer.MIN_VALUE) return Integer.MIN_VALUE;
                }
            }
        }

        if (sign) {
            return (int) result;
        } else {
            return (int) -result;
        }
    }

    private static boolean isDigit(char c) {
        return c >= '0' && c <= '9';
    }

    // Original - 12/23/2020 19:27
    // Not efficient at all - 9 ms
    private static int myAtoi01(String s) {
        if (s.isBlank()) return 0;
        s = s.trim();
        if (s.length() == 1) {
            if (Character.isDigit(s.charAt(0))) return Integer.parseInt(s);
            else return 0;
        }
        char firstChar = s.charAt(0);

        if (firstChar == 45 || firstChar == 43 || Character.isDigit(firstChar)) {
            char[] chars = s.toCharArray();
            for (int i = 1; i < chars.length; i++) {
                if (!Character.isDigit(chars[i])) {
                    if (!Character.isDigit(chars[i - 1])) {
                        return 0;
                    }
                    s = s.substring(0, i);
                    break;
                }
            }
            try {
                return Integer.parseInt(s);
            } catch (Exception e) {
                if (firstChar == '-') {
                    return Integer.MIN_VALUE;
                } else {
                    return Integer.MAX_VALUE;
                }
            }
        }

        return 0;
    }

}
