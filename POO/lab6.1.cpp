//
// Created by flawreen on 3/31/23.
//
#include <iostream>
#include <cmath>
using namespace std;

class Shape {
public:
	Shape() {
		cout << "shape\n";
	}
	virtual double compute_perimeter() const = 0;
	virtual double compute_area() const = 0;
	~Shape() {
		cout << "~shape\n";
	}
};

class Triangle : public Shape {
	double baza, h;
public:
	Triangle() : baza(0), h(0) {cout << "triangle\n";}
	Triangle(double baza, double h) : baza(baza), h(h) {cout << "triangle\n";}
	Triangle(const Triangle& t) : baza(t.baza), h(t.h) {}
	~Triangle() {
		cout << "~triangle\n";
	}
	double compute_area() const override {
		double area = (baza * h) / 2;
		return area;
	}
	double compute_perimeter() const override {
		return 0;
	}
};

class Rectangle : public Shape {
	double latime, lung;
public:
	Rectangle() : latime(0), lung(0) {cout << "rectangle\n";}
	Rectangle(double latime, double lung) : latime(latime), lung(lung) {cout << "rectangle\n";}
	Rectangle(const Rectangle& r) : latime(r.latime), lung(r.lung) {}
	~Rectangle() {
		cout << "~rectangle\n";
	}
	double compute_perimeter() const override {
		double perimetru = 2 * (latime + lung);
		return perimetru;
	}

	double compute_area() const override {
		double arie = lung * latime;
		return arie;
	}
};

class Circle : public Shape {
	double raza;
public:
	Circle() : raza(0) {cout << "circle\n";}
	Circle(double raza) : raza(raza) {cout << "circle\n";}
	Circle(const Circle& c) : raza(c.raza) {}
	~Circle() {
		cout << "~circle\n";
	}
	double compute_perimeter() const override {
		double peri = 2 * raza * M_PI;
		return peri;
	}
	double compute_area() const override {
		double area = raza * raza * M_PI;
		return area;
	}

};

//int main() {
//	Circle cerc(3);
//	Triangle tr(5, 10);
//	Rectangle drept(4, 5);
//
//	Shape* sh = &cerc;
//	cout << sh->compute_area();
//
//	cout << endl;
//	return 0;
//}
