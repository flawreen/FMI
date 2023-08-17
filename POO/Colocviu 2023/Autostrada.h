//
// Created by flawreen on 5/30/23.
//

#ifndef COLOCVIU2023_AUTOSTRADA_H
#define COLOCVIU2023_AUTOSTRADA_H
#include <string>
#include <iostream>
using namespace std;
#include "Drum.h"

class Autostrada : public Drum {
	int nrBenzi;
public:
	Autostrada();
	Autostrada(const string& denumire, const double lungime, const int nrTronsoane, const int nrBenzi);
	~Autostrada();
	Autostrada& operator=(Autostrada& drum);
	Autostrada& operator=(const Autostrada& drum);
	Autostrada(Autostrada& drum);
	Autostrada(const Autostrada& drum);
	friend ostream &operator<<(ostream &os, const Autostrada& drum);
	friend istream &operator>>(istream &is, Autostrada& drum);

	int getNrBenzi() const;

	void setNrBenzi(int nrBenzi);

	double getLungime();

};

#endif //COLOCVIU2023_AUTOSTRADA_H
