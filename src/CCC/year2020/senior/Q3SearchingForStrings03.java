package CCC.year2020.senior;

import xyz.scottc.scu.MathUtils;

import java.math.BigInteger;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * Faster than Method02 but need tons of memories.
 * It can handle any String if you have infinite RAM.
 */
public class Q3SearchingForStrings03 {

    private static final Set<String> PERMUTATIONS = new HashSet<>();
    private static boolean complete = false;
    private static BigInteger times;

    // should be 26
    public static void main(String[] args) {
        // Read the Test File
        String[] inputs = Q3SearchingForStrings01.readFromTestFile();
        String target = inputs[0];
        times = MathUtils.factorial(target.length());

        PERMUTATIONS.add(target);

        // Process the searching
        Thread handler = new Thread(new Handler(target));
        handler.start();

        // Counter
        Thread counter = new Thread(new Counter(inputs));
        counter.start();

    }

    private static class Handler implements Runnable {

        private final Set<String> possibilities = new HashSet<>();

        public Handler(String target) {
            this.possibilities.add(target);
        }

        @Override
        public void run() {
            while (!complete) {
                Set<String> temp = new HashSet<>(this.possibilities);
                for (String s : temp) {
                    for (int i = 0; i < s.length() - 1; i++) {
                        char[] chars = s.toCharArray();
                        char c;
                        c = chars[i];
                        chars[i] = chars[i + 1];
                        chars[i + 1] = c;
                        String result = new String(chars);
                        if (!PERMUTATIONS.contains(result))
                            this.possibilities.add(result);
                    }
                    this.possibilities.remove(s);
                }
                PERMUTATIONS.addAll(this.possibilities);
            }
            Thread.yield();
        }

    }

    private static class Counter implements Runnable {

        private final String[] inputs;

        public Counter(String[] inputs) {
            this.inputs = inputs;
        }

        @Override
        public void run() {
            List<Integer> sizeList = new ArrayList<>();
            while (!complete) {
                System.out.println(PERMUTATIONS.size() + " / " + times);
                sizeList.add(PERMUTATIONS.size());
                try {
                    Thread.sleep(100);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                if (this.getExistTimes(sizeList, PERMUTATIONS.size()) >= PERMUTATIONS.size() / 100) {
                    complete = true;
                    // Calculate the total exist amount
                    int total = 0;
                    for (String s : PERMUTATIONS) {
                        if (inputs[1].contains(s)) total++;
                    }
                    System.out.println(total);
                }
            }
            Thread.yield();
        }

        private int getExistTimes(List<Integer> targetList, int n) {
            int times = 0;
            for (int i : targetList) {
                if (i == n) times++;
            }
            return times;
        }
    }

}
