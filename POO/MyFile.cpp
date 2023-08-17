//
// Created by flawreen on 3/13/23.
//
#include <iostream>
#include <cstdio>
#include "MyFile.h"
using namespace std;

MyFile::MyFile(const char nume_fisier[]) {
		this->file = fopen(nume_fisier, "w");
}

MyFile::~MyFile() {
		fclose(file);
}

void MyFile::write(int numar) {
		fprintf(file, "%d\n", numar);
}

//int main() {
//	MyFile f("lab2/input.txt");
//	f.write(43);
//
//	return 0;
//}

