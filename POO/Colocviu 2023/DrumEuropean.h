//
// Created by flawreen on 5/30/23.
//

#ifndef COLOCVIU2023_DRUMEUROPEAN_H
#define COLOCVIU2023_DRUMEUROPEAN_H
#include <string>
#include <iostream>
using namespace std;
#include "Drum.h"

class DrumEuropean : public Drum {
	int nrTari;
public:
	DrumEuropean();
	DrumEuropean(const string& denumire, const double lungime, const int nrTronsoane, const int nrTari);
	~DrumEuropean();
	DrumEuropean& operator=(DrumEuropean& drum);
	DrumEuropean& operator=(const DrumEuropean& drum);
	DrumEuropean(DrumEuropean& drum);
	DrumEuropean(const DrumEuropean& druml);
	friend ostream &operator<<(ostream &os, const DrumEuropean& drum);
	friend istream &operator>>(istream &is, DrumEuropean& drum);

	int getNrTari() const;


};



#endif //COLOCVIU2023_DRUMEUROPEAN_H
