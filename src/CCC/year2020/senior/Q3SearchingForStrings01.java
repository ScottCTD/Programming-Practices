package CCC.year2020.senior;

import xyz.scottc.scu.SCConstants;
import xyz.scottc.scu.io.FileUtils;

import java.io.File;
import java.io.IOException;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;

/**
 * This method is the fastest one of the three maybe.
 * But... It cannot handle the String longer than 7.
 */
public class Q3SearchingForStrings01 implements SCConstants {

    protected static List<String> permutations = new ArrayList<>();
    protected static BigInteger times;

    public static void main(String[] args) {
        String[] inputs = readFromTestFile();
        String target = inputs[0];
        permutations.add(target);
        times = factorial(target.length());

/*        for (BigInteger i = new BigInteger("0"); i.compareTo(times) < 0; i = i.add(BigInteger.ONE)) {
            if (BigInteger.valueOf(permutations.size()).equals(times)) break;
            List<String> temp = new ArrayList<>(permutations);
            Collections.reverse(temp);
            for (int j = 0; j < target.length() - 1; j++) {
                if (j < temp.size()) findAllPermutations(temp.get(j));
            }
        }*/

        findAllPermutations(target);

        int amount = 0;
        for (String permutation : permutations) {
            if (inputs[1].contains(permutation)) {
                amount++;
            }
        }
        System.out.println(amount);
    }

    private static void findAllPermutations(String target) {
        if (times.equals(BigInteger.valueOf(permutations.size()))) return;
        if (times.compareTo(BigInteger.valueOf(permutations.size())) < 0) throw new RuntimeException("Invalid size!");
        String[] results = new String[target.length() - 1];
        for (int i = 0; i < target.length() - 1; i++) {
            char[] targetArray = target.toCharArray();
            char temp;
            temp = targetArray[i];
            targetArray[i] = targetArray[i + 1];
            targetArray[i + 1] = temp;
            String result = new String(targetArray);
            results[i] = result;
        }
        for (String temp : results) {
            if (!permutations.contains(temp)) {
                permutations.add(temp);
                findAllPermutations(temp);
            }
        }
    }

    protected static BigInteger factorial(long target) {
        BigInteger result = new BigInteger("1");
        for (long i = 1; i <= target; i++) {
            result = result.multiply(BigInteger.valueOf(i));
        }
        return result;
    }

    protected static String[] readFromTestFile() {
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
