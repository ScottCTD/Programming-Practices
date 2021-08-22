package LeetCode;

/**
 * This question was solved by C
 */
public class Q20 {

    public static void main(String[] args) {
        System.out.println(isValid("(([]){})"));
    }

    // Not original and inefficient
    private static boolean isValid(String s) {
        if (s.length() <= 1 || s.length() % 2 != 0)
            return false;
        int length = s.length() / 2;
        for (int i = 0; i < length; i++) {
            s = s.replace("()", "").replace("[]", "").replace("{}", "");
        }
        return s.isEmpty();
    }

}
