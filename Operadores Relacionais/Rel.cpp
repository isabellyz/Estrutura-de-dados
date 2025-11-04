#include <iostream>
using namespace std;

int main() {
    int a = 7;
    int b = 5;

    cout << "a = " << a << ", b = " << b << "\n\n";
    cout << "a < b  -> " << (a < b)  << "\n";
    cout << "a > b  -> " << (a > b)  << "\n";
    cout << "a <= b -> " << (a <= b) << "\n";
    cout << "a >= b -> " << (a >= b) << "\n";
    cout << "a == b -> " << (a == b) << "\n";
    cout << "a != b -> " << (a != b) << "\n";

    if (a > b) {
        cout << "\ndecisao: a (" << a << ") eh maior que b (" << b << ").\n";
    } else if (a < b) {
        cout << "\ndecisao: a (" << a << ") eh menor que b (" << b << ").\n";
    } else {
        cout << "\ndecisao: a (" << a << ") eh igual a b (" << b << ").\n";
    }
    return 0;
}