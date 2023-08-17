//
// Created by flawreen on 5/30/23.
//

#ifndef COLOCVIU2023_DRUM_H
#define COLOCVIU2023_DRUM_H
#include <string>
#include <iostream>
using namespace std;


class Drum {
protected:
	string denumire;
	double lungime;
	int nrTronsoane;
public:
	Drum();
	Drum(const string& denumire, const double lungime, const int nrTronsoane);
	virtual ~Drum();
	Drum& operator=(Drum& drum);
	Drum& operator=(const Drum& drum);
	Drum(Drum& drum);
	Drum(const Drum& drum);
	friend ostream &operator<<(ostream &os, const Drum& drum);
	friend istream &operator>>(istream &is, Drum& drum);
	string& getDenumire();

	void setDenumire(const string &denumire);

	double getLungime() const;

	void setLungime(double lungime);

	void setNrTronsoane(int nrTronsoane);

	double getNrTronsoane();
};


#endif //COLOCVIU2023_DRUM_H
