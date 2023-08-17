/* seminar
int x(10) == int x{10} == int x = 10;
int z(); -> functie
int z{}; -> int cu constructor gol

class NumeLung;
auto* var = new NumeLung; <=> NumeLung* var = new NumeLung;

ca sa declar o adresa a unui nr:
 int nr = 2, y = 3;
 int* p = &nr;
 pt afisare: cout << p afiseaza o adresa, cout << *p dereferentiaza adresa si afiseaza nr
 p = &y;
 int& r = x;

 for (int x : v)  itereaza printr-un array cu x
    cout << x;
nu merge pentru un vector alocat dinamic

 nullptr(C++11) -> recomandat -> poate fi bagat doar in pointeri
 NULL(C++98) -> la examen
 int x = NULL; nu functioneaza corect
 int* y = NULL; merge, adresa nula
 int z = nullptr; eroare
 int* s = nullptr; merge

 struct Vector {....};
 Vector v;
 v.elem accesare
 Vector* pv;
 pv->elem <=> (*pv).elem  accesare

 Vector3d operator+(Vector3d o, Vector3d b);

 enum class Culoare { // enum de clase
    Alb, Negru
};
Culoare c = Culoare::Alb;


 int main() { cout << square(5); }
 int square(int x) { return x*x;}
    -> eroare
  int square(int x);
  int main() { cout << square(5); }
  int square(int x) {
    return x*x;
  }
  -> nu da eroare

 */
#include <iostream>
#include <cmath>
using namespace std;

class Complex {
    double re, im;

public:
    Complex() : re(0), im(0) {}

    Complex(double re1, double im1) : re(re1), im(im1) {}

    friend ostream& operator<<(ostream &out, const Complex& c) {
        out << c.re;
        out << " + " << c.im << "i\n";
        return out;
    }
    friend istream& operator>>(istream &in, Complex& c);

    Complex operator+(const Complex &c) const {
        Complex rez;
        rez.re = re + c.re;
        rez.im = im + c.im;
        return rez;
    }

    Complex operator-(const Complex &c) {
        Complex rez;
        rez.re = re - c.re;
        rez.im = im - c.im;
        return rez;
    }

    bool operator==(const Complex& c) const {
        if(re == c.re && im == c.im)
            return 1;
        else return 0;
    }

    bool operator!=(const Complex& c) const {
        if(re != c.re || im != c.im)
            return 1;
        else return 0;
    }

    static Complex from_polar(double modul, double unghi) {
        return Complex(modul * cos(unghi), modul * sin(unghi));
    }

    void setRe(double x) {
        re = x;
    }

    double getRe() {
        return re;
    }

    void setIm(double x) {
        im = x;
    }

    double getIm() {
        return im;
    }
};

istream& operator>>(istream &in, Complex& c) {
        in >> c.re;
        in >> c.im;
        return in;
}

void interschimba(int& a, int& b) {
	a ^= b;
	b = a ^ b;
	a = a ^ b;
}

void interschimba(int* a, int* b) {
	*a ^= *b;
	*b = *a ^ *b;
	*a = *a ^ *b;
}


//int main() {
//    Complex c(3.4, 0);
//    cout << c;
//    Complex c2 = Complex::from_polar(2, 0.5);
//    cout << c2;
//    Complex c3;
//    cin >> c3;
//    cout << c3;
//    Complex c4 = c - c3;
//    cout << c4;
//    cout << (c == c4);
//    return 0;
//}




