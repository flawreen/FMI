//
// Created by flawreen on 3/10/23.
//
using namespace std;
#ifndef POO_INTVECTOR_H
#define POO_INTVECTOR_H


class IntVector {
    int size, *data;
public:
    IntVector();
    IntVector(int k, int x=0);
    ~IntVector();
    IntVector(const IntVector& copy);
    void operator=(const IntVector& copy);
    friend ostream& operator<<(ostream& out, const IntVector& v);

};


#endif //POO_INTVECTOR_H
