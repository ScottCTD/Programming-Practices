package CCC.year2020.senior;

import xyz.scottc.scu.MathUtils;

import java.math.BigInteger;
import java.util.HashSet;
import java.util.Set;

public class Q3SearchingForStrings03 {

    private static final Set<String> PERMUTATIONS = new HashSet<>();
    private static boolean complete = false;
    private static BigInteger times;

    public static void main(String[] args) {
        // Read the Test File
        String[] inputs = Q3SearchingForStrings01.readFromTestFile();
        String target = inputs[0];
        times = MathUtils.factorial(target.length());

        // Process the searching
        Thread handler = new Thread(new Handler(target));
        handler.setPriority(Thread.MAX_PRIORITY);
        handler.start();

        // Counter
        //Thread counter = new Thread(new Counter());
        //counter.start();

        while (!complete) {
            if (times.compareTo(BigInteger.valueOf(PERMUTATIONS.size())) == 0) {
                System.out.println(PERMUTATIONS);
                complete = true;

                // Calculate the total exist amount
                int total = 0;
                for (String s : PERMUTATIONS) {
                    if (inputs[1].contains(s)) total++;
                }
                System.out.println(total);
            }
        }
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
                            possibilities.add(result);
                    }
                    this.possibilities.remove(s);
                }
                PERMUTATIONS.addAll(this.possibilities);
            }
        }

    }

    private static class Counter implements Runnable {

        @Override
        public void run() {
            while (true) {
                System.out.println(
                        BigInteger.valueOf(PERMUTATIONS.size()).divide(times)
                );
                try {
                    Thread.sleep(5000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }
    }

}
