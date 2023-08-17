#include <iostream>
// constantin.majeri@s.unibuc.ro
using namespace std;

/*
 * gcc.godbolt.com
sizeof() - compile time
Tipuri de date:
 bool, char, short, int, long, long long, float, double


+++ generarea clasei
class Nume {
    int x;
};
+++ daca nu folosim clasa, nu se genereaza niciun cod in spate

// daca avem si int main:
int main() {
    Nume variabila; // nimic
    return 0; // mov $0, %eax
}


class Nume {
public:
    int x;

    int aduna() {
        return x + 1;
    }
};

int main() {
    Nume var; // se aloca 4B (probabil pe stiva) pt ca are doar un int
    var.x = 3; // aici se suprapun cei 4B alocati mai sus
    int rez = var.aduna(); // echivalent cu Nume::aduna(var);
    cout << rez;

    return 0;
}


++++ enum
enum Culoare {
    Alb,
    Negru
}
Culoare c = Alb;

*/


