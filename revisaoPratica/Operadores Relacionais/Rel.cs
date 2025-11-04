using System;

class Relacionais {
    static void Main() {
        int a = 7;
        int b = 5;

        Console.WriteLine($"a = {a}, b = {b}\n");
        Console.WriteLine($"a < b  -> {a < b}");
        Console.WriteLine($"a > b  -> {a > b}");
        Console.WriteLine($"a <= b -> {a <= b}");
        Console.WriteLine($"a >= b -> {a >= b}");
        Console.WriteLine($"a == b -> {a == b}");
        Console.WriteLine($"a != b -> {a != b}");

        if (a > b) {
            Console.WriteLine($"\ndecisao: a ({a}) e maior que b ({b}).");
        } else if (a < b) {
            Console.WriteLine($"\ndecisao: a ({a}) e menor que b ({b}).");
        } else {
            Console.WriteLine($"\ndecisao: a ({a}) e igual a b ({b}).");
        }
    }
}