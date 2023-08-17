//
// Created by flawreen on 5/30/23.
//

#include "DrumNational.h"

DrumNational::DrumNational() {

}

DrumNational::DrumNational(const string &denumire, const double lungime, const int nrTronsoane, const int nrJudete) : Drum(denumire, lungime, nrTronsoane), nrJudete(nrJudete) {

}

DrumNational &DrumNational::operator=(DrumNational &drum) {
	denumire = drum.denumire;
	lungime = drum.lungime;
	nrTronsoane = drum.nrTronsoane;
	nrJudete = drum.nrJudete;
	return *this;
}

DrumNational &DrumNational::operator=(const DrumNational &drum) {
	denumire = drum.denumire;
	lungime = drum.lungime;
	nrTronsoane = drum.nrTronsoane;
	nrJudete = drum.nrJudete;
	return *this;
}

DrumNational::DrumNational(DrumNational &drum) {
	denumire = drum.denumire;
	lungime = drum.lungime;
	nrTronsoane = drum.nrTronsoane;
	nrJudete = drum.nrJudete;
}

DrumNational::DrumNational(const DrumNational &drum) {
	denumire = drum.denumire;
	lungime = drum.lungime;
	nrTronsoane = drum.nrTronsoane;
	nrJudete = drum.nrJudete;
}

ostream &operator<<(ostream &os, const DrumNational &drum) {
	os << "Denumire: " << drum.denumire << endl;
	os << "Lungime drum: " << drum.lungime << endl;
	os << "Numar tronsoane: " << drum.nrTronsoane << endl;
	os << "Trece prin " << drum.nrJudete << " judete" << endl;
	return os;
}

istream &operator>>(istream &is, DrumNational &drum) {
	cout << "Introduceti denumirea drumului:";
	getline(is, drum.denumire);
	cout << "Introduceti lungimea drumului:";
	is >> drum.lungime;
	is.get();
	cout << "Introduceti numarul de tronsoane ale drumului:";
	is >> drum.nrTronsoane;
	is.get();
	cout << "Introduceti numarul de judete prin care trece:";
	is >> drum.nrJudete;
	is.get();
	return is;
}

DrumNational::~DrumNational() {

}
