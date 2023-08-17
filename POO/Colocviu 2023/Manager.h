//
// Created by flawreen on 5/30/23.
//

#ifndef COLOCVIU2023_MANAGER_H
#define COLOCVIU2023_MANAGER_H
#include <vector>
#include <string>
using namespace std;
#include "Drum.h"
#include "DrumEuropean.h"
#include "DrumNational.h"
#include "Autostrada.h"
#include "Contract.h"
#include "AutostradaDrumEuropean.h"


class Manager {
	vector<Drum*> drumuri;
	vector<Contract> contracte;

	static Manager* manager;
	Manager() = default;
	Manager(Manager& manager) = default;
	Manager(const Manager& manager) = default;
	Manager& operator=(Manager& manager) = default;
	Manager& operator=(const Manager& manager) = default;
public:
	static Manager* getInstance() {
		if (manager == nullptr) {
			manager = new Manager();
		}
		return manager;
	}

	void deleteInstance() {
		if (manager != nullptr) {
			delete manager;
		}
		manager = nullptr;
	}

	void adaugaDrum();
	void adaugaContract();
	void afiseazaDrumuri();
	void afiseazaContracte();
};


#endif //COLOCVIU2023_MANAGER_H
