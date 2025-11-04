public class Relacionais {
    public static void main(String[] args) {
        int a = 7;
        int b = 5;

        System.out.println("a = " + a + ", b = " + b + "\n");
        System.out.println("a < b  -> " + (a < b));
        System.out.println("a > b  -> " + (a > b));
        System.out.println("a <= b -> " + (a <= b));
        System.out.println("a >= b -> " + (a >= b));
        System.out.println("a == b -> " + (a == b));
        System.out.println("a != b -> " + (a != b));

        if (a > b) {
            System.out.println("\ndecisao: a (" + a + ") e maior que b (" + b + ").");
        } else if (a < b) {
            System.out.println("\ndecisao: a (" + a + ") e menor que b (" + b + ").");
        } else {
            System.out.println("\ndecisao: a (" + a + ") e igual a b (" + b + ").");
        }
    }
}