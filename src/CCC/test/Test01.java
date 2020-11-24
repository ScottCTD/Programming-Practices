package CCC.test;

import xyz.scottc.scu.StringUtils;

public class Test01 {

    public static void main(String[] args) {
        String target = "aab";
        String source = "abacabaa";

        int existAmountA = StringUtils.getExistTimes(target, "a");
        int existAmountB = StringUtils.getExistTimes(target, "b");

        int total = 0;

        int a = 0, b = 0;

        char[] chars = source.toCharArray();
        for (int i = 0; i < chars.length; i++) {
            if (chars[i] == 'a') a++;
            if (chars[i] == 'b') b++;
        }

        if (a == existAmountA && b == existAmountB) {

        }
    }
}
