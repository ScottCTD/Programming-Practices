package LeetCode;

/**
 * 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
 * 进阶：不转为字符串进行操作
 */
public class Q9 {

    public static void main(String[] args) {
        int x = 1234567899;
        System.out.println(isPalindrome02(x));
    }

    // Original
    // Very effective -> LeetCode 9 ms
    // Reached advanced requirement.
    private static boolean isPalindrome02(int x) {
        // Special case
        if (x == 0) return true;
        if (x < 0) return false;

        int result = 0;
        int temp = x;
        while (temp != 0) {
            result = result * 10 + temp % 10;
            temp /= 10;
        }
        return result == x;
    }

    // Original
    // Ineffective
    // Not achieve advanced requirement.
    private static boolean isPalindrome01(int x) {
        String s = String.valueOf(x);
        return s.equals(new String(reverseArray(s.toCharArray())));
    }

    private static char[] reverseArray(char[] array) {
        char[] newArr = new char[array.length];
        int index = 0;
        for (int i = array.length - 1; i >= 0; i--) {
            newArr[index] = array[i];
            index++;
        }
        return newArr;
    }

}
