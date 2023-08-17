//
// Created by flawreen on 3/6/23.
//

#ifndef POO_INTLIST_H
#define POO_INTLIST_H

#include <iostream>
using namespace std;

class IntList {
	class Node {
	public:
		int value;
		Node* next;
		Node();
		~Node();
		Node(const Node& cpy);
//		Node& operator=(const Node& cpy);
	};

	Node* head;
	int size;
public:
	IntList();
	IntList(const int* arr, int len);
	~IntList();
	IntList(const IntList& cpy);
	IntList operator+(IntList& list2);
	IntList& operator=(const IntList& cpy);
	int operator[] (int poz); // accesare dupa index
	int search (int x);
	void lappend(int x);
	void rappend(int x);

	friend ostream& operator<<(ostream& os, IntList& list);
};


#endif //POO_INTLIST_H
