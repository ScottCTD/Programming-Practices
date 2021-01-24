package CCC.year2020.senior.Q3SearchingForStrings;

/**
 * 011/13/2020 20:20
 */
public class Q3SearchingForStrings04 {

    public static void main(String[] args) {
        int result = searchingForStrings(new String[]{"abcdefghigijklmn", ""});
        System.out.println(result);
    }

    private static int searchingForStrings(String[] inputs) {
        return search(inputs[1], 0, new StringBuilder(), new boolean[inputs[0].length()], inputs[0].toCharArray());
    }

    // 01/24/2021 21:43
    // DFS
    private static int search(String hayStack, int result, StringBuilder builder, boolean[] used, char[] chars) {
        if (builder.length() == chars.length) {
            System.out.println(builder.toString());
            if (hayStack.contains(builder.toString())) {
                return ++result;
            }
            return result;
        }
        for (int i = 0; i < chars.length; i++) {
            if (used[i]) {
                continue;
            }
            if (i > 0 && used[i - 1] && chars[i] == chars[i - 1]) {
                continue;
            }
            builder.append(chars[i]);
            used[i] = true;
            result = search(hayStack, result, builder, used, chars);
            builder.deleteCharAt(builder.length() - 1);
            used[i] = false;
        }
        return result;
    }


}
