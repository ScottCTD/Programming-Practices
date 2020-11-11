package CCC.year2020.senior;

import xyz.scottc.scu.ArrayUtils;
import xyz.scottc.scu.MapUtils;
import xyz.scottc.scu.SCConstants;
import xyz.scottc.scu.io.FileUtils;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Q1SurmisingASprintersSpeed {

    // The answer should be 8853.570251923056
    public static void main(String[] args) {
        // Accept Input
        String rawInputs = null;
        try {
            rawInputs = FileUtils.readFileAsString(
                    new File("TestFiles/2020Q1.in"));
        } catch (IOException exception) {
            exception.printStackTrace();
        }

        // Read the input
        int amount = Integer.parseInt(rawInputs.trim().substring(0, rawInputs.indexOf("\n")).trim());
        Map<Integer, Integer> inputs = new HashMap<>(amount);
        rawInputs = rawInputs.substring(rawInputs.indexOf("\n") + 1);
        int index = 0;
        for (int i = 0; i < amount; i++) {
            int temp = rawInputs.indexOf(SCConstants.SPACE, index);
            int t = Integer.parseInt(rawInputs.substring(index, temp));
            int temp2 = rawInputs.indexOf("\n", index);
            int x = Integer.parseInt(rawInputs.substring(temp + 1, temp2 != -1 ? temp2 : rawInputs.length()));
            inputs.put(t, x);
            index = rawInputs.indexOf("\n", index) + 1;
        }

        // Sort the inputs according to the time (Ascent)
        Map<Integer, Integer> sortedInputs = MapUtils.sortMapByKeys(inputs);
        List<Integer> times = new ArrayList<>(sortedInputs.keySet());
        List<Integer> positions = new ArrayList<>(sortedInputs.values());

        // Find the max speed
        double[] speeds = new double[amount];
        for (int i = 0; i < sortedInputs.size() - 1; i++) {
            speeds[i] = findSpeed(times.get(i), positions.get(i), times.get(i + 1), positions.get(i + 1));
        }
        double max = ArrayUtils.max(speeds);

        System.out.println(max);
    }

    public static double findSpeed(int t1, int x1, int t2, int x2) {
        double dT = t2 - t1;
        double dX = x2 - x1;
        return Math.abs(dX / dT);
    }

}
