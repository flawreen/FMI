//
// Created by flawreen on 5/30/23.
//

#include "AutostradaDrumEuropean.h"

AutostradaDrumEuropean::AutostradaDrumEuropean() {

}

AutostradaDrumEuropean::AutostradaDrumEuropean(const string &denumire, const double lungime, const int nrTronsoane, const int nrBenzi, const int nrTari) : Drum(denumire, lungime, nrTronsoane), nrBenzi(nrBenzi), nrTari(nrTari) {

}

AutostradaDrumEuropean &AutostradaDrumEuropean::operator=(AutostradaDrumEuropean &drum) {
	denumire = drum.denumire;
	lungime = drum.lungime;
	nrTronsoane = drum.nrTronsoane;
	nrBenzi = drum.nrBenzi;
	nrTari = drum.nrTari;
	return *this;
}

AutostradaDrumEuropean &AutostradaDrumEuropean::operator=(const AutostradaDrumEuropean &drum) {
	denumire = drum.denumire;
	lungime = drum.lungime;
	nrTronsoane = drum.nrTronsoane;
	nrBenzi = drum.nrBenzi;
	nrTari = drum.nrTari;
	return *this;
}

AutostradaDrumEuropean::AutostradaDrumEuropean(AutostradaDrumEuropean &drum) {
	denumire = drum.denumire;
	lungime = drum.lungime;
	nrTronsoane = drum.nrTronsoane;
	nrBenzi = drum.nrBenzi;
	nrTari = drum.nrTari;
}

AutostradaDrumEuropean::AutostradaDrumEuropean(const AutostradaDrumEuropean &drum) {
	denumire = drum.denumire;
	lungime = drum.lungime;
	nrTronsoane = drum.nrTronsoane;
	nrBenzi = drum.nrBenzi;
	nrTari = drum.nrTari;
}

ostream &operator<<(ostream &os, const AutostradaDrumEuropean &drum) {
	os << "Denumire: " << drum.denumire << endl;
	os << "Lungime drum: " << drum.lungime << endl;
	os << "Numar tronsoane: " << drum.nrTronsoane << endl;
	os << "Are " << drum.nrBenzi << " benzi" << endl;
	os << "Trece prin " << drum.nrTari << " tari" << endl;
	return os;
}

istream &operator>>(istream &is, AutostradaDrumEuropean &drum) {
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
	cout << "Introduceti numarul de tari prin care trece:";
	is >> drum.nrTari;
	is.get();
	return is;
}

int AutostradaDrumEuropean::getNrBenzi() const {
	return nrBenzi;
}

void AutostradaDrumEuropean::setNrBenzi(int nrBenzi) {
	AutostradaDrumEuropean::nrBenzi = nrBenzi;
}

int AutostradaDrumEuropean::getNrTari() const {
	return nrTari;
}

void AutostradaDrumEuropean::setNrTari(int nrTari) {
	AutostradaDrumEuropean::nrTari = nrTari;
}

AutostradaDrumEuropean::~AutostradaDrumEuropean() {

}
