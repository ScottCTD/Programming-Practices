package LeetCode;

public class Q12 {

    public static void main(String[] args) {

        System.out.println(intToRoman02(1994));

    }

    // Not original
    // Little more efficient than mine
    // But the codes are much more cleaner
    public static String intToRoman02(int num) {
        int[] nums = new int[]{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] roman = new String[]{"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        String result = "";
        for (int i = 0; i < nums.length; i++) {
            while (num >= nums[i]) {
                num -= nums[i];
                result += roman[i];
            }
        }
        return result;
    }

    // Original
    // Not very efficient but it's ok
    // But the codes are really stupid
    public static String intToRoman01(int num) {
        String result = "";
        int remain;

        int M = num / 1000;
        for (int i = 0; i < M; i++) {
            result += "M";
        }

        remain = (num - M * 1000);
        int D = remain / 500, dTemp = D * 500;

        for (int i = 0; i < D; i++) {
            if (remain >= 900) {
                result += "CM";
                dTemp = 900;
                break;
            }
            result += "D";
        }

        remain -= dTemp;
        int C = remain / 100, cTemp = C * 100;
        for (int i = 0; i < C; i++) {
            if (remain >= 400) {
                result += "CD";
                cTemp = 400;
                break;
            }
            result += "C";
        }

        remain -= cTemp;
        int L = remain / 50, lTemp = L * 50;
        for (int i = 0; i < L; i++) {
            if (remain >= 90) {
                result += "XC";
                lTemp = 90;
                break;
            }
            result += "L";
        }

        remain -= lTemp;
        int X = remain / 10, xTemp = X * 10;
        for (int i = 0; i < X; i++) {
            if (remain >= 40) {
                result += "XL";
                xTemp = 40;
                break;
            }
            result += "X";
        }

        remain -= xTemp;
        int V = remain / 5, vTemp = V * 5;
        for (int i = 0; i < V; i++) {
            if (remain >= 9) {
                result += "IX";
                vTemp = 9;
                break;
            }
            result += "V";
        }

        remain -= vTemp;
        int I = remain / 1;
        for (int i = 0; i < I; i++) {
            if (remain >= 4) {
                result += "IV";
                break;
            }
            result += "I";
        }

        return result;
    }

}
