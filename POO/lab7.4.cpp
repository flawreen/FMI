#include <iostream>
#include <vector>
using namespace std;

class Product {
protected:
	double price;
public:

	virtual double get_price();
	virtual ~Product();
};

class PerishableProduct : public Product {
protected:
	bool expira;
public:
	void setExpira(const bool b) {
		expira = b;
	}

	double get_price() override {
		if (expira) return Product::get_price() - Product::get_price() * 0.1;
		else return Product::get_price();
	}
};

class ProductOnSale : public Product {
protected:
	double discount;
public:
	void setDiscount(const double d) {
		discount = d;
	}

	double get_price() override {
		return Product::get_price() - Product::get_price() * discount;
	}
};

class PerishableProductOnSale : public PerishableProduct, public ProductOnSale {
public:
	double get_price() override {
		ProductOnSale::setDiscount(ProductOnSale::discount + 0.1);
		return ProductOnSale::get_price();
	}
};


