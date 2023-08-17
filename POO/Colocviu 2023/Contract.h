//
// Created by flawreen on 5/30/23.
//

#ifndef COLOCVIU2023_CONTRACT_H
#define COLOCVIU2023_CONTRACT_H
#include <string>
#include <iostream>
using namespace std;


class Contract {
	string numeContract;
	string cif;
	int numar;
	string numeDrumAsociat;
	int nrTronson;
	double cost;
public:
	void setCost(double cost);

private:
	static int id_unic;
public:
	Contract();
	Contract(const string& numeContract, const string& cif);
	~Contract();
	Contract& operator=(Contract& contr);
	Contract& operator=(const Contract& contr);
	Contract(Contract& contr);
	Contract(const Contract& contr);
	friend ostream &operator<<(ostream &os, const Contract& contr);
	friend istream &operator>>(istream &is, Contract& contr);

	const string &getNumeContract() const;
	void setNumeContract(const string &numeContract);
	const string &getCif() const;
	void setCif(const string &cif);
	int getNumar() const;
	void setNumar(int numar);
	const string &getNumeDrumAsociat() const;
	void setNumeDrumAsociat(const string &numeDrumAsociat);
	int getNrTronson() const;
	void setNrTronson(int nrTronson);

	double getCost() const;

};


#endif //COLOCVIU2023_CONTRACT_H
