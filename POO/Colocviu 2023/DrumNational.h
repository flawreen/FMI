//
// Created by flawreen on 5/30/23.
//

#ifndef COLOCVIU2023_DRUMNATIONAL_H
#define COLOCVIU2023_DRUMNATIONAL_H
#include <string>
#include <iostream>
using namespace std;
#include "Drum.h"


class DrumNational : public Drum {
	int nrJudete;
public:
	DrumNational();
	DrumNational(const string& denumire, const double lungime, const int nrTronsoane, const int nrJudete);
	~DrumNational();
	DrumNational& operator=(DrumNational& drum);
	DrumNational& operator=(const DrumNational& drum);
	DrumNational(DrumNational& drum);
	DrumNational(const DrumNational& druml);
	friend ostream &operator<<(ostream &os, const DrumNational& drum);
	friend istream &operator>>(istream &is, DrumNational& drum);

};


#endif //COLOCVIU2023_DRUMNATIONAL_H
