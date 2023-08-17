#include <iostream>
#include <vector>
#include <string>

using namespace std;

/*
 produs perisabil, promotie; citire, stocare, afisare, constructori param, virtual etc.
 vectori de pointeri catre clasa de baza care contine derivate
 la pointeri destructorii nu se apeleaza automat, trebuie cu delete
 la upcasting si downcasting trebuie destructor virtual
 */

// MOSTENIREA IN DIAMANT
class Produs {
protected:
	string denumire;

public:
	virtual void citire();

	friend ostream &operator<<(ostream &os, const Produs &);
};

class Promotie : virtual public Produs {
protected:
	float discount;
public:
	void citire();

	friend ostream &operator<<(ostream &os, const Promotie &p);
};

class Perisabil : virtual public Produs {
protected:
	string expirare;
public:
	void citire();

	friend ostream &operator<<(ostream &os, const Perisabil &p);
};

class PeriPromo : public Promotie, public Perisabil {
public:
	void citire();

	friend ostream &operator<<(ostream &os, const PeriPromo &p);
};


//int main() {
//	vector<Produs*> v;
//	int n;
//	cin >> n;
//	for (int i = 0; i < n; ++i) {
//		int op;
//		cin >> op;
//		if (op == 1) v.push_back(new Produs());
//		else if (op == 2) v.push_back(new Perisabil());
//		else if (op == 3) v.push_back(new Promotie());
//		else v.push_back(new PeriPromo());
//	}
//
//	/*
//	Produs *p;
//	p = new PeriPromo();
//	p->citire();
//	cout << *p; // chiar daca avem cout pt PeriPromo, il fol pe cel pt Produs
//	// pt ca face la compilare
//	cout << dynamic_cast<PeriPromo*>(p); // asa afiseaza adresa
//	cout << *dynamic_cast<PeriPromo*>(p); // cu dereferentiere merge
//	return 0;
//	 */
//
//}

void Produs::citire() { cin >> denumire; }

void Promotie::citire() {
	Produs::citire();
	cin >> discount;
}

void Perisabil::citire() {
	Produs::citire();
	cin >> expirare;
}

void PeriPromo::citire() {
	Promotie::citire();
	cin >> expirare;
}

ostream &operator<<(ostream &os, const Produs &p) {
	os << p.denumire << " ";
	return os;
	// return os << p.denumire << " "; // varianta compacta
}

ostream &operator<<(ostream &os, const PeriPromo &p) {
	return os << p.denumire << " " << p.discount << " " << p.expirare << " ";
}
