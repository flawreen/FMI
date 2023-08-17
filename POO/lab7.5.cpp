//
// Created by flawreen on 4/7/23.
//

#include <iostream>
#include "ex1.cpp"
using namespace std;

class Labelable {
	string label;
public:
	string getLabel() {
		return label;
	}
	void setLabel(string s) {
		label = s;
	}
	Labelable() = default;

};
