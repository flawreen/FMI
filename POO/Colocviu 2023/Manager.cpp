//
// Created by flawreen on 5/30/23.
//

#include "Manager.h"

void Manager::adaugaDrum() {
	string optiune;
	cout << "Tip de drum (National/European/Autostrada/AutostradaDrumEuropean)";
	getline(cin, optiune);
	if (optiune == "National") {
		Drum *drum = new DrumNational();
		cin >> *drum;
		drumuri.push_back(drum);
	} else if (optiune == "European") {
		Drum *drum = new DrumEuropean();
		cin >> *drum;
		drumuri.push_back(drum);
	} else if (optiune == "Autostrada") {
		Drum *drum = new Autostrada();
		cin >> *drum;
		drumuri.push_back(drum);
	} else if (optiune == "AutostradaDrumEuropean") {
		Drum *drum = new AutostradaDrumEuropean();
		cin >> *drum;
		drumuri.push_back(drum);
	}
}

void Manager::afiseazaDrumuri() {
	for (auto drum : drumuri) {
		cout << *drum << endl;
	}
}

void Manager::afiseazaContracte() {
	for (auto contr : contracte) {
		cout << contr << endl;
	}
}

void Manager::adaugaContract() {
	string nume;
	int tronson;
	string tipDrum;
	cout << "Tip drum (National/European/Autostrada/AutostradaDrumEuropean): ";
	getline(cin, tipDrum);
	cout << "Nume drum: ";
	getline(cin, nume);
	cout << "Numar tronson: ";
	cin >> tronson;

	for (auto drum : drumuri) {
		if (drum->getDenumire() == nume) {
			try {
				for (auto ctr: contracte) {
					if (ctr.getNrTronson() == tronson) throw string("Tronsonul deja exista!");
				}
				Contract ctr;
				cin >> ctr;
				ctr.setNrTronson(tronson);
				ctr.setNumeDrumAsociat(nume);
				if (tipDrum == "Autostrada" || tipDrum == "AutostradaDrumEuropean") {
					if (tipDrum == "Autostrada") {
						Autostrada *drumNou  = new Autostrada();
						drumNou = dynamic_cast<Autostrada *>(drum);
						ctr.setCost(2500 * drumNou->getNrBenzi() * (drumNou->getLungime() / drumNou->getNrTronsoane()));
					} else {
						AutostradaDrumEuropean *drumNou  = new AutostradaDrumEuropean();
						drumNou = dynamic_cast<AutostradaDrumEuropean *>(drum);
						ctr.setCost(2500 * drumNou->getNrBenzi() * (drumNou->getLungime() / drumNou->getNrTronsoane()));
					}
				} else {
					ctr.setCost(3000 * (drum->getLungime() / drum->getNrTronsoane()));
				}
				if (tipDrum == "European" || tipDrum == "AutostradaDrumEuropean") {
					if (tipDrum == "European") {
						DrumEuropean *drumNou  = new DrumEuropean();
						drumNou = dynamic_cast<DrumEuropean *>(drum);
						ctr.setCost(ctr.getCost() + 500 * drumNou->getNrTari());
					} else {
						AutostradaDrumEuropean *drumNou  = new AutostradaDrumEuropean();
						drumNou = dynamic_cast<AutostradaDrumEuropean *>(drum);
						ctr.setCost(ctr.getCost() + 500 * drumNou->getNrTari());
					}
				}
				contracte.push_back(ctr);
			} catch (const string& error) {
				cout << error << endl;
			}
		}
	}
}
