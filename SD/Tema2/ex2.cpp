//
// Created by flawreen on 6/1/23.
//

#include <iostream>
#include <string>
using namespace std;
/*
 (3p) 2. Creati o coada (double-ended queue = dequeue) in care sã se poatà
insera si extrage de la amble capete in timp constant. Folositi o implementare de list dublu inlantuitã de tipul
struct nod{int val; nod* prev; nod* next;} *stanga, *dreapta;
 */

struct Node {
	Node* prev;
	int val;
	Node* next;
} *stanga, *dreapta;


void pushTail(int valoare) {
	if (dreapta == nullptr) {
		dreapta = new Node();
		dreapta->val = valoare;
		stanga = dreapta;
		return;
	}
	dreapta->next = new Node();
	dreapta->next->prev = dreapta;
	dreapta->next->val = valoare;
	dreapta = dreapta->next;
}

void pushFront(int valoare) {
	if (stanga == nullptr) {
		stanga = new Node();
		stanga->val = valoare;
		dreapta = stanga;
		return;
	}
	stanga->prev = new Node();
	stanga->prev->next = stanga;
	stanga->prev->val = valoare;
	stanga = stanga->prev;
}

int getTail() {
	if (dreapta != nullptr) return dreapta->val;
}

int getFront() {
	if (stanga != nullptr) return stanga->val;
}

void afisare() {
	Node* p = stanga;
	while(p) {
		cout << p->val << " ";
		p = p->next;
	}
	cout << endl;
}

void popFront() {
	try {
		if (stanga == nullptr) throw string("Empty dequeue.");
		if (stanga -> next == nullptr) {
			delete stanga;
			stanga = nullptr;
			dreapta = nullptr;
			return;
		}

		stanga = stanga->next;
		delete stanga->prev;
		stanga->prev = nullptr;
	} catch (const string& error) {
		cout << error << endl;
	}
}

void popTail() {
	try {
		if (dreapta == nullptr) throw string("Empty dequeue.");
		if (dreapta -> prev == nullptr) {
			delete dreapta;
			dreapta = nullptr;
			stanga = nullptr;
			return;
		}

		dreapta = dreapta->prev;
		delete dreapta->next;
		dreapta->next = nullptr;
	} catch (const string& error) {
		cout << error << endl;
	}
}

int main() {
	popFront(); // Empty dequeue.
	pushTail(5);
	pushTail(7);
	pushFront(6);
	pushFront(1);
	pushFront(2);
	pushTail(10);
	afisare(); // 2 1 6 5 7 10
	cout << getFront() << endl; // 2
	cout << getTail() << endl; // 10
	popFront();
	afisare(); // 1 6 5 7 10
	popTail();
	afisare(); // 1 6 5 7

	return 0;
}
