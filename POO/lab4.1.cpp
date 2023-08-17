#include <iostream>
using namespace std;

class Date {
	int ziua, luna, anul;
public:
	Date(int zi, int luna, int an) : ziua(zi), luna(luna), anul(an) {}

	int getZiua() const {
		return ziua;
	}

	int getLuna() const {
		return luna;
	}

	int getAnul() const {
		return anul;
	}
};

class DateInterval {
	Date d1, d2;
public:
	DateInterval(int zi1, int luna1, int an1, int zi2, int luna2, int an2) :
		d1(zi1, luna1, an1), d2(zi2, luna2, an2) {}
	int ani() const {
		const int ani = d2.getAnul() - d1.getAnul();
		return ani;
	}
	int decenii() {
		const int anii = ani();
		const int deceniu = anii / 10;
		return deceniu;
	}

};

//int main() {
//	const int x = 5;
//	int y = 6;
//	int y2 = 7;
////	int& xx = x;
//	const int& xxx = x;
//	const int& yy = y;
//
//	const int& a = 42;
//	int* p = &y;
//	p = &y2;
////	int* q = &x;
//	const int* qq = &y;
//	qq = &y2;
//	const int* const g = &y;
//
//	const Date d(3, 4, 2002);
//
//
//
//	return 0;
//}