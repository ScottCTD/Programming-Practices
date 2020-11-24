package CCC.year2019.senior;

public class Q1Flipper {

    public static void main(String[] args) {
        Q1Flipper q1Flipper = new Q1Flipper();
        q1Flipper.start(args);
    }

    public void start(String[] args) {
        Grid grid = new Grid();
        String output = grid.flip("VHV");
        System.out.println(output);
    }

    private static class Grid {

        public int upperLeft = 1;
        public int upperRight = 2;
        public int lowerLeft = 3;
        public int lowerRight = 4;

        public String flip(String input) {
            if (input.length() < 1 || input.length() > 1000000) {
                throw new RuntimeException("Invalid Input String!");
            }
            for (char t : input.toCharArray()) {
                if (t == 'H') {
                    this.flipHorizontally();
                } else if (t == 'V') {
                    this.flipVertically();
                } else {
                    throw new RuntimeException("Invalid Input String!");
                }
            }
            return this.toString();
        }

        private void flipHorizontally() {
            int temp;
            temp = this.upperLeft;
            this.upperLeft = this.lowerLeft;
            this.lowerLeft = temp;

            temp = this.upperRight;
            this.upperRight = this.lowerRight;
            this.lowerRight = temp;
        }

        private void flipVertically() {
            int temp;
            temp = this.upperLeft;
            this.upperLeft = this.upperRight;
            this.upperRight = temp;

            temp = this.lowerLeft;
            this.lowerLeft = this.lowerRight;
            this.lowerRight = temp;
        }

        @Override
        public String toString() {
            return this.upperLeft + "\t" + this.upperRight + "\n" +
                    this.lowerLeft + "\t" + this.lowerRight;
        }
    }

}
