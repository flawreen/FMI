#include <iostream>
#include <cstring>
#include "String.h"
using namespace std;

String::String() {
    str = nullptr;
}

String::String(const char *s) {
    size = strlen(s);
    str = new char[size+1];
    strncpy(str, s, size);
}

String::String(const String& cpy) {
    if (str != nullptr) {
		delete[] str;
	}
	size = cpy.size;
	strcpy(str, cpy.str);
}

String::~String() {
    if (nullptr != str) {
            delete[] str;
    }
}

String String::operator+ (const String& a) {
    String concat;
    const int size_new = a.size + size;
    char* str2;
    str2 = new char[size_new+1];
    strncpy(str2, str, size);
    strncpy(str2+size, a.str, a.size);
    str2[size_new] = '\0';
    concat.str = str2;
    concat.size = size_new;
    return concat;
}

ostream &operator<<(ostream &os, String &str) {
    os << str.str;
    return os;
}

String &String::operator+=(const char s) {
    char *str2;
    str2 = new char[size+2];
    strncpy(str2, str, size);
    str2[size] = s;
    str2[size+1] = '\0';
    delete[] str;
    str = str2;
    size+= 1;
    return *this;
}

void String::operator[](const char *substr) {
    char* rezultat = strstr(this->str, substr);
    if (rezultat == nullptr) {
        cout << "Sirul nu a fost gasit.";
    } else {
        cout << rezultat;
    }
}

String &String::operator=(const String &cpy) {
	if (str != nullptr) {
		delete[] str;
	}
	size = cpy.size;
	strcpy(str, cpy.str);
	return *this;
}

//int main() {
//    String sir("Ana are");
//    cout << sir << endl;
//
//    // copiere
//    String sir2("mere");
//    cout << sir2 << endl;
//
//    // append
//	sir += ' ';
//    sir += '2';
//	sir += ' ';
//    cout << sir << endl;
//
//    // concatenare
//    String concatenare = sir + sir2;
//    cout << concatenare << endl;
//
//    //  cautare
//    sir["a"];
//
//
//    return 0;
//}
