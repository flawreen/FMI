//
// Created by flawreen on 3/6/23.
//

#include "IntList.h"

IntList::Node::Node() {
	next = nullptr;
}

IntList::Node::~Node() {
	delete next;
}

IntList::Node::Node(const IntList::Node &cpy) {
	value = cpy.value;
	next = cpy.next;
}

IntList::IntList() {
	head = nullptr;
	size = 0;
}

//IntList::IntList(const int* arr) {
//	size = sizeof(*arr);
//	Node *p = new Node; // fac un pointer pentru parcurgere
//	head = new Node; // initializez head
//	end = new Node;
//	head->value = arr[0];
//	head->next = p; // head pointeaza la pointerul de parcurgere
//	for (int i = 1; i < size; ++i) {
//		if(i < size-2) {
//			p->value = arr[i];
//			p->next = new Node; // daca e ultimul element nu are destinatie
//			p = p->next;
//		} else if(i == size-2) {
//			end = new Node;
//			p->next = end; // incerc sa fac un pointer catre final
//			p->value = arr[i];
//		} else {
//			end->value = arr[i];
//		}
////		end->value = p->value;
////		end->next = p->next;
//	}
//}



IntList::IntList(const int* arr, const int len) {
	size = len;
	Node* p = new Node; // pointerul de parcurgere
	head = new Node; // pointerul de inceput
	head->value = arr[0];
	head->next = p;
	for (int i = 1; i < size; ++i) {
		p->value = arr[i];
		if (i < size-1) {
			p->next = new Node;
			p = p->next;
		}
	}
}

IntList::IntList(const IntList &cpy) {
	size = cpy.size;
	Node* p = new Node; // parcurg cpy
	p = cpy.head->next;
	Node* q = new Node; // parcurg this
	head = new Node;
	head->value = cpy.head->value;
	head->next = q;
	while (p != nullptr) {
		q->value = p->value;
		if (p->next != nullptr) {
			q->next = new Node;
			q = q->next;
		}
		p = p->next;
	}
}

IntList &IntList::operator=(const IntList &cpy) {
	size = cpy.size;
	Node* p = new Node; // parcurg cpy
	p = cpy.head->next;
	Node* q = new Node; // parcurg this
	head = new Node;
	head->value = cpy.head->value;
	head->next = q;
	while (p != nullptr) {
		q->value = p->value;
		if (p->next != nullptr) {
			q->next = new Node;
			q = q->next;
		}
		p = p->next;
	}
}


IntList::~IntList() {
	delete head;
}

ostream &operator<<(ostream &os, IntList& list) {
	if (list.head == nullptr) os << "Lista este vida.";
	else {
		IntList::Node *p = list.head;
		while (p) {
			os << p->value << " ";
			p = p->next;
		}
	}
	return os;
}

int IntList::operator[](const int poz) {
	int i = 0;
	Node *p = head;
	while (i < poz) {
		if (p->next != nullptr) {
			++i;
			p = p->next;
		} else {
			cout << "Index " << poz << " out of bounds.\n";
			return -1;
		}
	}
	return p->value;
}

int IntList::search(int x) {
	int i = 0;
	Node* p = head;
	while (p->value != x) {
		if (p->next != nullptr) {
			++i;
			p = p->next;
		} else if (p->value != x) return -1;
	}
	return i;
}

void IntList::lappend(int x) {
	Node* p = new Node;
	p->next = head;
	p->value = x;
	head = p;
}

void IntList::rappend(int x) {
	Node* p;
	p = head;
	while (p->next != nullptr) {
		p = p->next;
	}
	p->next = new Node;
	p = p->next;
	p->value = x;
}

IntList IntList::operator+(IntList &list2) {
	Node* p; // cu p parcurg this
	Node* q; // cu q parcurg list2
	p = head;
	q = list2.head;
	while (p->next != nullptr) {
		p = p->next;
	}
	while (q != nullptr) {
		p->next = new Node;
		p = p->next;
		p->value = q->value;
		q = q->next;
	}
	return *this;
}

//int main() {
//	int arr[] = {3, 2, 3, 4};
//	IntList lista(arr, 4);
//	cout << lista << endl;
//	cout << lista[1] << endl;
//	cout << lista.search(4) << endl;
//	IntList lista2(lista);
//	cout << lista2 << endl;
//	lista.lappend(6);
//	cout << lista << endl;
//	lista.rappend(7);
//	cout << lista << endl;
//
//	lista = lista + lista2;
//	cout << lista;
//	return 0;
//}
