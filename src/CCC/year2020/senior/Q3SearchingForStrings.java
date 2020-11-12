package CCC.year2020.senior;

import xyz.scottc.scu.SCConstants;
import xyz.scottc.scu.io.FileUtils;

import java.io.File;
import java.io.IOException;

public class Q3SearchingForStrings implements SCConstants {

    public static void main(String[] args) {

    }

    private static String[] findAllPermutations(String target) {
        int times = factorial(target.length());

        return;
    }

    private static int factorial(int target) {
        int result = target;
        for (int i = target - 1; i > 0; i--) {
            result *= i;
        }
        return result;
    }

    private static String[] readFromTestFile() {
        try {
            String rawInput = FileUtils.readFileAsString(new File("TestFiles/2020Q3.in"));
            String[] inputs = new String[2];
            int index = rawInput.indexOf("\n");
            inputs[0] = rawInput.substring(0, index).trim();
            inputs[1] = rawInput.substring(index + 1).trim();
            return inputs;
        } catch (IOException exception) {
            exception.printStackTrace();
        }
        return new String[2];
    }

}
