//
// Created by flawreen on 5/30/23.
//

#include "Contract.h"
int Contract::id_unic = 0;

Contract::Contract() {
    ++id_unic;
	numar = id_unic;
}

Contract::Contract(const string &numeContract, const string &cif) : numeContract(numeContract),
cif(cif) {
    ++id_unic;
	numar = id_unic;
}

Contract::~Contract() {

}

Contract &Contract::operator=(Contract &contr) {
	numeContract = contr.numeContract;
	cif = contr.cif;
	numar = contr.numar;
	cost = contr.cost;
	return *this;
}

Contract &Contract::operator=(const Contract &contr) {
	numeContract = contr.numeContract;
	cif = contr.cif;
	numar = contr.numar;
	cost = contr.cost;
	return *this;
}

const string &Contract::getNumeContract() const {
	return numeContract;
}

void Contract::setNumeContract(const string &numeContract) {
	Contract::numeContract = numeContract;
}

const string &Contract::getCif() const {
	return cif;
}

void Contract::setCif(const string &cif) {
	Contract::cif = cif;
}

int Contract::getNumar() const {
	return numar;
}

void Contract::setNumar(int numar) {
	Contract::numar = numar;
}

const string &Contract::getNumeDrumAsociat() const {
	return numeDrumAsociat;
}

void Contract::setNumeDrumAsociat(const string &numeDrumAsociat) {
	Contract::numeDrumAsociat = numeDrumAsociat;
}

int Contract::getNrTronson() const {
	return nrTronson;
}

void Contract::setNrTronson(int nrTronson) {
	Contract::nrTronson = nrTronson;
}


Contract::Contract(Contract &contr) {
	numeContract = contr.numeContract;
	cif = contr.cif;
	numar = contr.numar;
	cost = contr.cost;

}

Contract::Contract(const Contract &contr) {
	numeContract = contr.numeContract;
	cif = contr.cif;
	numar = contr.numar;
	cost = contr.cost;

}

ostream &operator<<(ostream &os, const Contract &contr) {
	os << "Denumire: " << contr.numeContract << endl;
	os << "CIF: " << contr.cif << endl;
	os << "Numar contract: " << contr.numar << endl;
	return os;
}

istream &operator>>(istream &is, Contract &contr) {
	cout << "Introduceti numele contractului: ";
	getline(is, contr.numeContract);
	cout << "Introduceti CIF: ";
	getline(is, contr.cif);
	return is;
}

void Contract::setCost(double cost) {
	Contract::cost = cost;
}

double Contract::getCost() const {
	return cost;
}

