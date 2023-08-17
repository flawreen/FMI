//
// Created by flawreen on 5/30/23.
//

#include "DrumEuropean.h"


DrumEuropean::DrumEuropean() {

}

DrumEuropean::DrumEuropean(const string &denumire, const double lungime, const int nrTronsoane, const int nrTari) : Drum(denumire, lungime, nrTronsoane), nrTari(nrTari) {

}

DrumEuropean &DrumEuropean::operator=(DrumEuropean &drum) {
	denumire = drum.denumire;
	lungime = drum.lungime;
	nrTronsoane = drum.nrTronsoane;
	nrTari = drum.nrTari;
	return *this;
}

DrumEuropean &DrumEuropean::operator=(const DrumEuropean &drum) {
	denumire = drum.denumire;
	lungime = drum.lungime;
	nrTronsoane = drum.nrTronsoane;
	nrTari = drum.nrTari;
	return *this;
}

DrumEuropean::DrumEuropean(DrumEuropean &drum) {
	denumire = drum.denumire;
	lungime = drum.lungime;
	nrTronsoane = drum.nrTronsoane;
	nrTari = drum.nrTari;
}

DrumEuropean::DrumEuropean(const DrumEuropean &drum) {
	denumire = drum.denumire;
	lungime = drum.lungime;
	nrTronsoane = drum.nrTronsoane;
	nrTari = drum.nrTari;
}

ostream &operator<<(ostream &os, const DrumEuropean &drum) {
	os << "Denumire: " << drum.denumire << endl;
	os << "Lungime drum: " << drum.lungime << endl;
	os << "Numar tronsoane: " << drum.nrTronsoane << endl;
	os << "Trece prin " << drum.nrTari << " tari" << endl;
	return os;
}

istream &operator>>(istream &is, DrumEuropean &drum) {
	cout << "Introduceti denumirea drumului:";
	getline(is, drum.denumire);
	cout << "Introduceti lungimea drumului:";
	is >> drum.lungime;
	is.get();
	cout << "Introduceti numarul de tronsoane ale drumului:";
	is >> drum.nrTronsoane;
	is.get();
	cout << "Introduceti numarul de tari prin care trece:";
	is >> drum.nrTari;
	is.get();
	return is;
}

DrumEuropean::~DrumEuropean() {

}

int DrumEuropean::getNrTari() const {
	return nrTari;
}


