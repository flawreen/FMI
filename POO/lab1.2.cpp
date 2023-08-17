/* Constructori si destructori
public, protected, private

class Gol {};
in main: Gol variabila; // chiar daca n-avem constructor, apeleaza compilatorul un constr care nu face nimic

 class UnConstructor {
    UnConstructor(int x) {}
};
in main: UnConstructor variabila; eroare de compilare, pt ca avem variabila in clasa

++ ca sa luam constructorul default inapoi
class UnConstructor {
    UnConstructor() {}
    UnConstructor(int x) {}
};
 */
#include <iostream>
using namespace std;

enum Culoare {
    Alb,
    Negru
};

class Nebun {
    // totul e private din oficiu
    int rand, coloana;
    // char coloana; pt a5 b6 etc
    Culoare culoare;
public:
    Nebun() { // constructor implicit al clasei: Nebun nebun1;
        rand = 1;
        coloana = 2;
        culoare = Alb;
    }

    Nebun(Culoare c) {  // Nebun nebun(Negru);
        rand = 1;
        coloana = 2;
        culoare = c;
    }

    ~Nebun() {  // Destructor
        cout << "bye" << endl;
    }

    void set_rand(int r) {  // setter
        rand = r;
    }

};

void inter(int* a, int* b) {
	int aux = *a;
}

void f() {
    Nebun n;
    cout << "functie" << endl;
    //  se sterge variabila n aici deci se afiseaza "functie", apoi "bye"
}



