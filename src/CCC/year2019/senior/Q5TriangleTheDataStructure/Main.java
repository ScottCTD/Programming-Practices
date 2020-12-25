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

}
