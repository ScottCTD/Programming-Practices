package LeetCode;

import java.util.ArrayList;
import java.util.List;

public class Q6 {

    public static void main(String[] args) {
        String result = convert02("LEETCODEISHIRING", 3);
        System.out.println(result);
        System.out.println(result.equals("LCIRETOESIIGEDHN"));
    }

    // Original
    // Relatively effective -> 6 ms
    // Same method as convert01
    // but with better logic and way to iterate
    private static String convert02(String s, int numRows) {
        if (numRows == 1) return s;
        if (s.length() == 0) return "";

        char[] chars = s.toCharArray();
        // 2 is a special case for my method, so let it alone.
        if (numRows == 2) {
            StringBuilder builder = new StringBuilder();
            for (int i = 0; i < chars.length; i += 2) {
                builder.append(chars[i]);
            }
            for (int i = 1; i < chars.length; i += 2) {
                builder.append(chars[i]);
            }
            return builder.toString();
        }

        StringBuilder[] builders = new StringBuilder[numRows];
        for (int i = 0; i < builders.length; i++) {
            builders[i] = new StringBuilder();
        }
        int y = 0, index = 0;
        for (char aChar : chars) {
            if (index < numRows) {
                builders[y].append(aChar);
                if (y + 1 < numRows) y++;
                index++;
            } else {
                y--;
                builders[y].append(aChar);
                if (y == 1) {
                    index = 0;
                    y--;
                }
            }
        }
        StringBuilder result = new StringBuilder();
        for (StringBuilder builder : builders) {
            result.append(builder.toString());
        }

        return result.toString();
    }

    // Original
    // Not very effective -> 9 ms
    // Use an array of char lists to visualize the grid
    // then, put every character in zigzag formation
    // Lastly, orderly iterate the array to get the fianl result
    private static String convert01(String s, int numRows) {
        if (numRows == 1) return s;
        if (s.length() == 0) return "";

        if (numRows == 2) {
            StringBuilder builder = new StringBuilder();
            char[] chars = s.toCharArray();
            for (int i = 0; i < chars.length; i += 2) {
                builder.append(chars[i]);
            }
            for (int i = 1; i < chars.length; i += 2) {
                builder.append(chars[i]);
            }
            return builder.toString();
        }

        int specialSize = numRows - 2;
        List<Character>[] temp = new List[numRows];
        // Init temp
        for (int i = 0; i < numRows; i++) {
            temp[i] = new ArrayList<>();
        }

        char[] chars = s.toCharArray();
        int index = 0, times = 0;
        for (char aChar : chars) {
            if (times == numRows + specialSize) times = 0;
            if (times < numRows) {
                temp[index].add(aChar);
                index++;
                times++;
            } else {
                if (index == numRows) index--;
                index--;
                temp[index].add(aChar);
                times++;
                if (index == 1) index = 0;
            }
        }

        StringBuilder result = new StringBuilder();
        for (List<Character> characters : temp) {
            for (int j = 0; j < characters.size(); j++) {
                result.append(characters.get(j));
            }
        }

        return result.toString();
    }

}
