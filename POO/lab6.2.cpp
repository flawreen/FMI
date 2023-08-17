#include <iostream>
using namespace std;
#include <string>

class Masina {
	string nume;
	static int nrMasini;
public:
	Masina() : nume(""){
		++nrMasini;
	}
	Masina(string nume) : nume(nume) {
		++nrMasini;
	}
	Masina(const Masina& m) : nume(m.nume) {
		++nrMasini;
	}
	~Masina() {
		--nrMasini;
	}
	static int getNrMasini() {
		return nrMasini;
	}
};
int Masina::nrMasini = 0;

//int main() {
//	Masina a, b, c, d, e;
//	cout << Masina::getNrMasini();
//
//	return 0;
//}
