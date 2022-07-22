package LeetCode;

/**
 * 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
 * 123 -> 321
 * -123 -> -321
 */
public class Q7 {

    public static void main(String[] args) {
        System.out.println(reverse02(-123));
    }

    // Unoriginal
    // The best method.
    // Same idea as mine.
    private static int reverse03(int x) {
        long result = 0;
        while (x != 0) {
            result = result * 10 + x % 10;
            x /= 10;
        }
        return (int) result == result ? (int) result : 0;
    }

    // Original
    // 2ms in LeetCode
    /*
    Conclude in 12/25/2020 18:28
    Idea:
    123 / 10 = 12
    12 / 10 = 1

    123 % 10 = 3
    12 % 10 = 2
    1 % 10 = 1

    loop 1: 3
    loop 2: 3 * 10 + 12 % 10 = 32
    loop 3: 3 * 10 + 12 % 10 + 1 % 10 = 321
     */
    private static int reverse02(int x) {
        long result = 0;
        long multiplier = 10;
        int len = x < 0 ? String.valueOf(x).length() - 1 : String.valueOf(x).length();

        for (int i = len - 1; i >= 0; i--) {
            result += x % multiplier / (multiplier / 10) * Math.pow(10, i);
            multiplier *= 10;
        }

        if (result > Integer.MAX_VALUE || result < Integer.MIN_VALUE) return 0;
        return (int) result;
    }

    // Orginal
    // Not efficient.
    private static int reverse01(int x) {
        try {
            String input = String.valueOf(x);
            char[] chars = input.toCharArray();

            if (chars[0] == '-') {
                char[] temp = reverseArray(chars, 1);
                return -Integer.parseInt(new String(temp));
            }

            char[] temp = reverseArray(chars, 0);
            return Integer.parseInt(new String(temp));
        } catch (Exception e) {
            return 0;
        }
    }

    private static char[] reverseArray(char[] array, int from) {
        char[] newArr = new char[array.length - from];
        int index = 0;
        for (int i = array.length - 1; i >= from; i--) {
            newArr[index] = array[i];
            index++;
        }
        return newArr;
    }

}
