package CCC.year2019.senior.Q5TriangleTheDataStructure;

import java.util.List;

public class Main {

    public static void main(String[] args) {
        Triangle triangle = new Triangle(1, new int[] {1000000000});

        List<Triangle> triangles = triangle.getAllSubtriangle(1);
        int total = 0;
        for (Triangle sub : triangles) {
            int max = sub.getMax();
            total += max;
        }
        System.out.println(total);
    }

    public static void sort(int[] target) {
        for (int i = 0; i < target.length; i++) {
            for (int j = 0; j < target.length - 1; j++) {
                if (target[j] < target[j + 1]) continue;
                int temp = target[j];
                target[j] = target[j + 1];
                target[j + 1] = temp;
            }
        }
    }

    public static void fill(int[] target) {
        for (int i = 0; i < target.length; i++) {
            target[i] = (int) (1000 * Math.random());
        }
    }

}
