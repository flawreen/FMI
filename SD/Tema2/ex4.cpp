//
// Created by flawreen on 6/3/23.
//

#include <iostream>
#include <vector>
#include <stack>
using namespace std;

int main() {
	vector<int> v;
	stack<int> stiva;
	int n;
	cin >> n;
	vector<int> frecv(n);
	for (int i = 0; i < n; ++i) {
		int x;
		cin >> x;
		v.push_back(x);
	}
	for (auto x : v) {
		cout << x << " ";
	}
	cout << endl;

	for (auto x : v) {
		if (frecv[x] == 1) { // elementul a mai aparut
			if (stiva.top() == x) {  // daca este in varful stivei inseamna ca firul acestuia nu se intersecteaza cu alt fir si ii pot da pop din stiva
				stiva.pop();
				++frecv[x];
			} else {
				cout << "Configuratie invalida.\n";
				return 0;
			}
		} else if (frecv[x] == 0) {  // marchez prima aparitie si il adaug in stiva
			++frecv[x];
			stiva.push(x);
		}
	}
	if (!stiva.empty()) cout << "Configuratie invalida.\n"; // Daca au ramas valori in stiva inseamna ca ori au ramas tarusi fara pereche ori se intersecteaza anumite fire
	else cout << "Configuratie valida!\n";

	return 0;
}
