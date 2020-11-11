package CCC.year2020.senior;

import xyz.scottc.scu.ArrayUtils;
import xyz.scottc.scu.SCConstants;
import xyz.scottc.scu.io.FileUtils;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.*;

public class Q1SurmisingASprintersSpeed {

    public static void main(String[] args) {
        // Accept Input
        FileInputStream inputStream = null;
        StringBuilder builder = new StringBuilder();
        try {
            inputStream = new FileInputStream("C:\\Users\\Scott\\Downloads\\Compressed\\all_data\\senior_data\\s1\\s1.2-09.in");
            int length;
            byte[] buffer = new byte[8192];
            while ((length = inputStream.read(buffer)) != -1) {
                builder.append(new String(buffer, 0, length));
            }
        } catch (IOException exception) {
            exception.printStackTrace();
        } finally {
            FileUtils.closeStreams(inputStream, null);
        }
        String rawInputs = builder.toString();

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
        Map<Integer, Integer> sortedInputs = new TreeMap<>(inputs);
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
