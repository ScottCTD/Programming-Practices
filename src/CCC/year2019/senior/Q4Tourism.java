package CCC.year2019.senior;

import xyz.scottc.scu.ArrayUtils;

public class Q4Tourism {

    public static void main(String[] args) {
        long t1 = System.currentTimeMillis();
        int test = findBestTotalScore(7, 3, new int[] {2, 4, 8, 7, 8, 10, 12});
        long t2 = System.currentTimeMillis();
        System.out.println("result = " + test);
        System.out.println("time = " + (t2 - t1));
    }

    public static int findBestTotalScore(int total, int maxPerDay, int[] scores) {
        int days = daysNeeded(total, maxPerDay);
        int bestTotalScore = 0;

        /*if the length of scores can be divide exactly by the maxPerDay, meaning that
        there is no special day in the scores array
        and the order of that array cannot be changed, so the result will be simply
        the total of every max value of every day*/
        if (scores.length % maxPerDay == 0) {
            for (int i = 0; i < scores.length; i += maxPerDay) {
                int[] perDay = new int[maxPerDay];
                for (int j = 0; j < maxPerDay; j++) {
                    perDay[j] = scores[i + j];
                }
                int max = ArrayUtils.max(perDay);
                bestTotalScore += max;
            }
            return bestTotalScore;
        }

        // all of the possible output
        int[] possibilities = new int[days];

        // the number of attractions of that special day (the day with less attractions)
        int specialDayTotalAttractionsAmount = total % maxPerDay;
        int[] specialDay = new int[specialDayTotalAttractionsAmount];

        // index is the start attraction of the special day
        // it will plus the maxPerDay after each possible combination
        int index = 0;
        for (int i = 0; i < days; i++) {

            // get the special day
            for (int j = 0; j < specialDay.length; j++) {
                specialDay[j] = scores[index + j];
            }

            // remove the special day array in the scores array
            // the result will be a very nice subject of recursion
            int[] before = new int[i * maxPerDay];
            for (int j = 0; j < before.length; j++) {
                before[j] = scores[j];
            }
            int[] after = new int[scores.length - specialDay.length - before.length];
            for (int j = 0; j < after.length; j++) {
                after[j] = scores[before.length + specialDay.length + j];
            }
            int[] newScores = ArrayUtils.combine(before, after);

            int totalBestScore = findBestTotalScore(total, maxPerDay, newScores);
            // the max score of that special day
            totalBestScore += ArrayUtils.max(specialDay);
            possibilities[i] = totalBestScore;

            index += maxPerDay;
        }

        // return the best score
        return ArrayUtils.max(possibilities);
    }

    public static int daysNeeded(int total, int maxPerDay) {
        if (total % maxPerDay != 0) {
            return total / maxPerDay + 1;
        }
        return total / maxPerDay;
    }

}
