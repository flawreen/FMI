//
// Created by flawreen on 3/13/23.
//

#ifndef POO_MYFILE_H
#define POO_MYFILE_H
#include <cstdio>
using namespace std;

class MyFile {
	FILE* file;
public:
	MyFile() = default;
	MyFile(const char nume_fisier[]);
	MyFile(const MyFile&) = delete;
	~MyFile();
	void write(int numar);
	MyFile& operator=(const MyFile&) = delete;

};


#endif //POO_MYFILE_H
