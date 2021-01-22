package LeetCode;

import java.util.Arrays;

/**
 * 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
 * <p>
 * "2", "3"
 * "123", "456"
 * "99", "99"
 */
public class Q43 {

    public static void main(String[] args) {
        System.out.println(multiply02("9999999999999999999", "231514523466325634568349567349756837469"));
    }

    // 01/22/2021 11:40
    // Almost original
    // 1 ms in LeetCode - Top Method
    // Instead of my dynamic carrier adding, this method handler carrier separately.
    // This is much more efficient and cleaner.
    public static String multiply02(String num1, String num2) {
        int length01 = num1.length(), length02 = num2.length(), length03 = length01 + length02;
        char[] chars01 = num1.toCharArray(), chars02 = num2.toCharArray(), result = new char[length03];
        Arrays.fill(result, '0');

        // Multiply but ignore carrier
        for (int i = length01 - 1; i >= 0; i--) {
            int n01 = chars01[i] - '0';
            for (int j = length02 - 1; j >= 0; j--) {
                int n02 = chars02[j] - '0';
                result[i + j + 1] += n01 * n02;
            }
        }
        // Handle carrier (>=10)
        for (int i = length03 - 1; i > 0; i--) {
            int n = result[i] - '0';
            if (n >= 10) {
                result[i - 1] += n / 10;
                result[i] = (char) (n % 10 + '0');
            }
        }
        // Form a string
        int i;
        for (i = 0; i < length03 - 1; i++) {
            if (result[i] != '0') {
                break;
            }
        }
        return new String(result, i, result.length - i);
    }

    // 01/22/2021 11:23
    // Original
    // Not very efficient - 9 ms in LeetCode
    // Dynamically add number and carrier to the result[]
    // Very difficult to do and not very efficient, but it's ok.
    public static String multiply01(String num1, String num2) {
        char zero = '0';
        int index01 = num1.length() - 1, index02 = num2.length() - 1;
        char[] result = new char[index01 + 1 + index02 + 1];
        Arrays.fill(result, zero);
        int a = 1, index = result.length - a++;
        while (index01 >= 0) {
            char c1 = num1.charAt(index01);
            char c2;
            if (index02 < 0) index02 = num2.length() - 1;
            c2 = num2.charAt(index02);
            int temp = (c1 - zero) * (c2 - zero), carrier = temp / 10, value = temp % 10;
            int offset = 0;
            while (carrier != 0 || value != 0) {
                temp = result[index - offset] - zero + value;
                value = temp % 10;
                carrier += temp / 10;
                result[index - offset] = (char) (value + zero);
                value = carrier;
                carrier = 0;
                offset++;
            }
            index02--;
            index--;
            if (index02 < 0) {
                index01--;
                index = result.length - a++;
            }
        }
        int offset;
        for (offset = 0; offset < result.length - 1; offset++) {
            if (result[offset] != '0') break;
        }
        return new String(result, offset, result.length - offset);
    }

}
