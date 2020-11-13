package CCC.year2020.senior;

public class Q3SearchingForStrings02 extends Q3SearchingForStrings01 {

    private static final StringBuilder BUILDER = new StringBuilder();
    private static boolean[] used;

    public static void main(String[] args) {
        String[] inputs = readFromTestFile();

        String target = inputs[0];
        used = new boolean[target.length()];
        findAllPermutations(target);
        System.out.println(permutations);

        int amount = 0;
        for (String permutation : permutations) {
            if (inputs[1].contains(permutation)) {
                amount++;
            }
        }
        System.out.println(amount);
    }

    private static void findAllPermutations(String target) {
        if (target.length() == BUILDER.length() && !permutations.contains(BUILDER.toString())) {
            permutations.add(BUILDER.toString());
            return;
        }
        for (int i = 0; i < target.length(); i++) {
            if (used[i]) continue;
            BUILDER.append(target.charAt(i));
            used[i] = true;
            findAllPermutations(target);
            used[i] = false;
            BUILDER.setLength(BUILDER.length() - 1);
        }
    }

}
