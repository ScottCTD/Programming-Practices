package CCC.year2019.senior.Q5TriangleTheDataStructure;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Triangle {

    // size = max row amount
    // start from 1
    private final int size;

    // every row is stored in rows
    private final List<int[]> rows = new ArrayList<>();

    private final int[] values;

    public Triangle(int size, int[] values) {
        this.size = size;
        this.values = values;
        int from = 0;
        for (int i = 1; i <= size; i++) {
            int[] row = Arrays.copyOfRange(values, from, from + i);
            from += i;
            this.rows.add(row);
        }
    }

    public List<Triangle> getAllSubtriangle(int size) {
        List<Triangle> subtriangles = new ArrayList<>();
        if (size == this.size) {
            subtriangles.add(this);
            return subtriangles;
        }

        // get the total amount of size=1 sub-triangle for given size
        int amount = this.getAmount(size);
        // iterate every size=1 triangle as the first size=1 triangle of every possible size=size triangle
        // outermost iteration, iterating the rows for the triangle
        for (int i = 0; i <= this.rows.size() - size; i++) {
            // iterate each column of the triangle
            for (int j = 0; j < this.rows.get(i).length; j++) {
                int[] values = new int[amount];
                int index = 0;
                // iterate the rows of one possible size=size triangle
                for (int k = 0; k < size; k++) {
                    /*iterate each column of that size=size triangle to exactly get
                    that triangle with values from the size = this.size triangle*/
                    for (int h = 0; h <= k; h++) {
                        /*h <= k -> Making sure the h = 0 can be iterated
                        * index > amount then break -> Making sure that h != k after
                        * the first iteration*/
                        if (index > amount) break;
                        values[index] = this.get(i + k, j + h);
                        index++;
                    }
                }
                subtriangles.add(new Triangle(size, values));
            }
        }
        return subtriangles;
    }

    public int getMax() {
        Arrays.sort(this.values);
        return this.values[this.values.length - 1];
    }

    public int getAmount(int size) {
        int total = 0;
        for (int i = 1; i <= size; i++) {
            for (int j = 1; j <= i; j++) {
                total++;
            }
        }
        return total;
    }

    public int get(int row, int index) {
        return this.rows.get(row)[index];
    }

    @Override
    public String toString() {
        StringBuilder builder = new StringBuilder();
        for (int[] values : this.rows) {
            for (int value : values) {
                builder.append(value).append(" ");
            }
            builder.append("\n");
        }
        return builder.toString();
    }
}
