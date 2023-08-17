//
// Created by flawreen on 5/30/23.
//

#ifndef COLOCVIU2023_AutostradaDrumEuropeanDRUMEUROPEAN_H
#define COLOCVIU2023_AutostradaDrumEuropeanDRUMEUROPEAN_H
#include <string>
#include <iostream>
using namespace std;
#include "Drum.h"

class AutostradaDrumEuropean : public Drum {
	int nrBenzi;
	int nrTari;
public:
	AutostradaDrumEuropean();
	AutostradaDrumEuropean(const string& denumire, const double lungime, const int nrTronsoane, const int nrBenzi, const int nrTari);
	~AutostradaDrumEuropean();
	AutostradaDrumEuropean& operator=(AutostradaDrumEuropean& drum);
	AutostradaDrumEuropean& operator=(const AutostradaDrumEuropean& drum);
	AutostradaDrumEuropean(AutostradaDrumEuropean& drum);
	AutostradaDrumEuropean(const AutostradaDrumEuropean& drum);
	friend ostream &operator<<(ostream &os, const AutostradaDrumEuropean& drum);
	friend istream &operator>>(istream &is, AutostradaDrumEuropean& drum);

	int getNrBenzi() const;

	void setNrBenzi(int nrBenzi);

	int getNrTari() const;

	void setNrTari(int nrTari);

};


#endif //COLOCVIU2023_AutostradaDrumEuropeanDRUMEUROPEAN_H
