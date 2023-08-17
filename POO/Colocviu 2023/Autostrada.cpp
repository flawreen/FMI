//
// Created by flawreen on 5/30/23.
//

#include "Autostrada.h"

Autostrada::Autostrada() {

}

Autostrada::Autostrada(const string &denumire, const double lungime, const int nrTronsoane, const int nrBenzi) : Drum(denumire, lungime, nrTronsoane), nrBenzi(nrBenzi) {

}

Autostrada &Autostrada::operator=(Autostrada &drum) {
	denumire = drum.denumire;
	lungime = drum.lungime;
	nrTronsoane = drum.nrTronsoane;
	nrBenzi = drum.nrBenzi;
	return *this;
}

Autostrada &Autostrada::operator=(const Autostrada &drum) {
	denumire = drum.denumire;
	lungime = drum.lungime;
	nrTronsoane = drum.nrTronsoane;
	nrBenzi = drum.nrBenzi;
	return *this;
}

Autostrada::Autostrada(Autostrada &drum) {
	denumire = drum.denumire;
	lungime = drum.lungime;
	nrTronsoane = drum.nrTronsoane;
	nrBenzi = drum.nrBenzi;
}

Autostrada::Autostrada(const Autostrada &drum) {
	denumire = drum.denumire;
	lungime = drum.lungime;
	nrTronsoane = drum.nrTronsoane;
	nrBenzi = drum.nrBenzi;
}

ostream &operator<<(ostream &os, const Autostrada &drum) {
	os << "Denumire: " << drum.denumire << endl;
	os << "Lungime drum: " << drum.lungime << endl;
	os << "Numar tronsoane: " << drum.nrTronsoane << endl;
	os << "Are " << drum.nrBenzi << " benzi" << endl;
	return os;
}

istream &operator>>(istream &is, Autostrada &drum) {
	cout << "Introduceti denumirea drumului:";
	getline(is, drum.denumire);
	cout << "Introduceti lungimea drumului:";
	is >> drum.lungime;
	is.get();
	cout << "Introduceti numarul de tronsoane ale drumului:";
	is >> drum.nrTronsoane;
	is.get();
	cout << "Introduceti numarul de benzi:";
	is >> drum.nrBenzi;
	is.get();
	return is;
}

int Autostrada::getNrBenzi() const {
	return nrBenzi;
}

void Autostrada::setNrBenzi(int nrBenzi) {
	Autostrada::nrBenzi = nrBenzi;
}

Autostrada::~Autostrada() {

}

double Autostrada::getLungime() {
	return lungime;

}
