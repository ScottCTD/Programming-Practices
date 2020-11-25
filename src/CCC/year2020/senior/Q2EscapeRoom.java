package CCC.year2020.senior;

import xyz.scottc.scu.SCConstants;
import xyz.scottc.scu.io.FileUtils;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * Maybe unstable because there are no test files available except the sample
 * The sample output should be "Yes"
 */
public class Q2EscapeRoom {

    public static void main(String[] args) {
        Grid grid = Grid.createGrid(new File("TestFiles/CCC/2020Q2.in"));
        try {
            boolean escape = canEscape(grid.get(0, 0), grid);
            if (escape) {
                System.out.println("Yes");
            } else {
                System.out.println("No");
            }
        } catch (StackOverflowError e) {
            System.out.println("No");
        }
    }

    private static boolean canEscape(int startValue, Grid grid) {
        List<int[]> all = getAllPossibleCoordinates(startValue, grid);
        boolean escaped = false;
        for (int[] p : all) {
            if (p[0] == grid.getRow() && p[1] == grid.getColumn()) return true;
            int temp = grid.get(p);
            // Unstable recursion, may produce stack over flow error
            // Why CCC dont give me the test files for this question?
            escaped = canEscape(temp, grid);
            if (escaped) break;
        }
        return escaped;
    }

    private static List<int[]> getAllPossibleCoordinates(int target, Grid grid) {
        List<int[]> coordinates = new ArrayList<>();
        for (int i = 1; i <= target; i++) {
            for (int j = 1; j <= target; j++) {
                if (i * j == target && i <= grid.getRow() + 1 && j <= grid.getColumn() + 1)
                    coordinates.add(new int[]{i - 1, j - 1});
            }
        }
        return coordinates;
    }

    private static class Grid implements SCConstants {

        private int row;
        private int column;
        private int[][] grid;

        private Grid(int row, int column, int[][] grid) {
            this.row = row - 1;
            this.column = column - 1;
            this.grid = grid;
        }

        public static Grid createGrid(File testFile) {
            try {
                String rawInput = FileUtils.readFileAsString(testFile).trim();
                int index = rawInput.indexOf("\n");
                int row = Integer.parseInt(rawInput.substring(0, index).trim());
                rawInput = rawInput.substring(index + 1).trim();
                index = rawInput.indexOf("\n");
                int column = Integer.parseInt(rawInput.substring(0, index).trim());
                rawInput = rawInput.substring(index + 1).trim();

                int[][] grid = new int[row][column];

                int start = 0;
                int stop = 0;

                rawInput = rawInput.replace("\n", SPACE);

                for (int i = 0; i < row; i++) {
                    for (int j = 0; j < column; j++) {
                        stop = rawInput.indexOf(SPACE, start) == -1 ? rawInput.length() : rawInput.indexOf(SPACE, start);
                        grid[i][j] = Integer.parseInt(rawInput.substring(start, stop));
                        start = stop + 1;
                    }
                }

                return new Grid(row, column, grid);

            } catch (IOException exception) {
                exception.printStackTrace();
            }
            throw new RuntimeException("Failed to create a Grid!");
        }

        public int get(int row, int column) {
            return grid[row][column];
        }

        public int get(int[] rowAndColumn) {
            return grid[rowAndColumn[0]][rowAndColumn[1]];
        }

        public int getRow() {
            return row;
        }

        public int getColumn() {
            return column;
        }
    }

}
