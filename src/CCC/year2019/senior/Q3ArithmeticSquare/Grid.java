package CCC.year2019.senior.Q3ArithmeticSquare;

import java.util.ArrayList;
import java.util.List;

/**
 * Unfinished
 * Because I didn't figure out how to properly do that...
 */
public class Grid {

    private final List<Object> data = new ArrayList<>(9);

    public Grid(Object[] values) {
        if (values.length != 9) throw new RuntimeException("Invalid Input!");

        for (int i = 0; i < values.length; i++) {
            Object value = values[i];
            this.data.add(value);
        }
    }

/*    public boolean checkHorizontally() {
        int index = 0;
        for (int i = 0; i < data.size(); i += 3) {
            
        }
    }

    public boolean checkVertically() {

    }*/

    @Override
    public String toString() {
        int index = 0;
        StringBuilder builder = new StringBuilder();
        for (Object obj : this.data) {
            builder.append(obj.toString()).append("\t");
            if (index++ == 2) {
                builder.append("\n");
                index = 0;
            }
        }
        return builder.toString();
    }
}
