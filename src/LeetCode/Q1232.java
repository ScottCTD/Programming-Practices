package LeetCode;

/**
 * 在一个XY 坐标系中有一些点，我们用数组coordinates来分别记录它们的坐标，其中coordinates[i] = [x, y]表示横坐标为 x、纵坐标为 y的点。
 * <p>
 * 请你来判断，这些点是否在该坐标系中属于同一条直线上，是则返回 true，否则请返回 false。
 * <p>
 * {1, 1}, {2, 2}, {3, 4}, {4, 5}, {5, 6}, {7, 7}
 * {1,2},{2,3},{3,4},{4,5},{5,6},{6,7}
 * {0, 0}, {0, 1}, {0, -1}
 */
public class Q1232 {

    public static void main(String[] args) {
        int[][] array = {{0, 0}, {0, 1}, {0, -1}};
        System.out.println(checkStraightLine(array));
    }

    // Original
    // Efficient - 0ms in LeetCode - Top Method
    public static boolean checkStraightLine(int[][] coordinates) {
        // Calculate slope
        int[] pos01 = coordinates[0], pos02 = coordinates[1];
        double dY = pos02[1] - pos01[1], dX = pos02[0] - pos01[0];
        double slope = dY / dX;
        boolean infinity = Double.isInfinite(slope);

        for (int i = 1; i < coordinates.length - 1; i++) {
            pos01 = coordinates[i];
            pos02 = coordinates[i + 1];
            dY = pos02[1] - pos01[1];
            dX = pos02[0] - pos01[0];
            double temp = dY / dX;
            if (temp != slope) {
                if (infinity && Double.isFinite(temp)) {
                    return false;
                } else if (infinity && Double.isInfinite(temp)) {
                    continue;
                }
                return false;
            }
        }
        return true;
    }

}
