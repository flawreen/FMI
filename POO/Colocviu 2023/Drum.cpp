//
// Created by flawreen on 5/30/23.
//

#include "Drum.h"

Drum::Drum() {

}

Drum::Drum(const string &denumire, const double lungime, const int nrTronsoane)  :
	denumire(denumire), lungime(lungime), nrTronsoane(nrTronsoane){

}

Drum::~Drum() {

}

Drum &Drum::operator=(Drum &drum) {
	denumire = drum.denumire;
	lungime = drum.lungime;
	nrTronsoane = drum.nrTronsoane;
	return *this;
}

Drum &Drum::operator=(const Drum &drum) {
	denumire = drum.denumire;
	lungime = drum.lungime;
	nrTronsoane = drum.nrTronsoane;
	return *this;
}

Drum::Drum(Drum &drum) {
	denumire = drum.denumire;
	lungime = drum.lungime;
	nrTronsoane = drum.nrTronsoane;
}

Drum::Drum(const Drum &drum) {
	denumire = drum.denumire;
	lungime = drum.lungime;
	nrTronsoane = drum.nrTronsoane;

}

ostream &operator<<(ostream &os, const Drum &drum) {
	os << "Denumire: " << drum.denumire << endl;
	os << "Lungime drum: " << drum.lungime << endl;
	os << "Numar tronsoane: " << drum.nrTronsoane << endl;
	return os;
}

istream &operator>>(istream &is, Drum &drum) {
	cout << "Introduceti denumirea drumului:";
	getline(is, drum.denumire);
	cout << "Introduceti lungimea drumului:";
	is >> drum.lungime;
	is.get();
	cout << "Introduceti numarul de tronsoane ale drumului:";
	is >> drum.nrTronsoane;
	is.get();
	return is;
}

string &Drum::getDenumire() {
	return denumire;
}

double Drum::getNrTronsoane() {
	return nrTronsoane;
}

void Drum::setDenumire(const string &denumire) {
	Drum::denumire = denumire;
}

double Drum::getLungime() const {
	return lungime;
}

void Drum::setLungime(double lungime) {
	Drum::lungime = lungime;
}

void Drum::setNrTronsoane(int nrTronsoane) {
	Drum::nrTronsoane = nrTronsoane;
}



