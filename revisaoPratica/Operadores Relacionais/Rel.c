#include <stdio.h>

int main() {
    int a = 7;
    int b = 5;

    printf("a = %d, b = %d\n\n", a, b);
    printf("a < b  -> %d\n", a < b);
    printf("a > b  -> %d\n", a > b);
    printf("a <= b -> %d\n", a <= b);
    printf("a >= b -> %d\n", a >= b);
    printf("a == b -> %d\n", a == b);
    printf("a != b -> %d\n", a != b);

    if (a > b) {
        printf("\ndecisao: a (%d) eh maior que b (%d).\n", a, b);
    } else if (a < b) {
        printf("\ndecisao: a (%d) eh menor que b (%d).\n", a, b);
    } else {
        printf("\ndecisao: a (%d) eh igual a b (%d).\n", a, b);
    }
    return 0;
}