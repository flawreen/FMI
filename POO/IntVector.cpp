//
// Created by flawreen on 3/10/23.
//
#include <iostream>
#include "IntVector.h"

void IntVector::operator=(const IntVector &copy) {
    if(data == nullptr)
            delete[] data;
    data = new int[copy.size];
    for (int i = 0; i < copy.size; ++i)
        data[i] = copy.data[i];
    size = copy.size;
}

IntVector::IntVector(const IntVector &copy) {
    data = new int[copy.size];
    for (int i = 0; i < copy.size; ++i)
        data[i] = copy.data[i];
    size = copy.size;
}

IntVector::~IntVector() {
    if(data != nullptr)
        delete[] data;
}

IntVector::IntVector(const int k, int x) {
    data = new int[k];
    for(int i = 0; i < k; ++i) {
        data[i] = x;
    }
    size = k;
}

IntVector::IntVector() : size(0), data(nullptr) {}

ostream &operator<<(ostream &out, const IntVector &v) {
    for (int i=0; i < v.size; ++i)
        out << v.data[i] << " ";
    return out;
}



//int main() {
//    IntVector v1;
//    IntVector v2(5, 3);
//    cout << v2 << endl;
//    IntVector v3=v2;
//    cout << v3 << endl;
//    IntVector v4(v2);
//    cout << v4 << endl;
//
//
//    return 0;
//}
