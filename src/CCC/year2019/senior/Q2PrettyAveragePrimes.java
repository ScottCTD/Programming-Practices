package CCC.year2019.senior;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Q2PrettyAveragePrimes {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        int cases = scanner.nextInt();
        if (cases < 1 || cases > 1000) {
            throw new RuntimeException("Invalid cases!");
        }
        int[] targets = new int[cases];
        int temp = 0;
        while (scanner.hasNextInt()) {
            int target = scanner.nextInt();
            targets[temp] = target;
            temp++;
            if (temp == cases) {
                break;
            }
        }

        for (int target : targets) {
            List<Output> outputs = Q2PrettyAveragePrimes.process(target);
            StringBuilder builder = new StringBuilder();
            for (Output output : outputs) {
                builder.append(output.toString()).append(" ");
            }
            System.out.println(builder);
        }

    }
    
    private static List<Output> process(int target) {
        List<Output> outputs = new ArrayList<>();
        for (int i = 2; i <= target * 2; i++) {
            if (Q2PrettyAveragePrimes.isPrimeNumber(i)) {
                for (int j = i; j <= target * 2; j++) {
                    if (Q2PrettyAveragePrimes.isPrimeNumber(j)) {
                        if (((double) i + (double) j) / 2D == (double) target) {
                            outputs.add(new Output(i, j));
                        }
                    }
                }
            }
        }
        return outputs;
    }

    private static boolean isPrimeNumber(int target) {
        for (int i = 2; i < target; i++) {
            if (target % i == 0) {
                return false;
            }
        }
        return true;
    }
    
    private static class Output {
        
        public int number01;
        public int number02;

        public Output(int number01, int number02) {
            this.number01 = number01;
            this.number02 = number02;
        }

        @Override
        public String toString() {
            return this.number01 + " " + this.number02;
        }
    }
}
