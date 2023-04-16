//
// Created by flawreen on 4/16/23.
//

#include <iostream>

using namespace std;

/*
 S ̆a se construiasc ̆a o list ̆a (prin una din procedurile de inserat elemente
ˆın list ̆a). Dup ̆a ce s-au citit toate elementele, s ̆a se parcurg ̆a lista s, i s ̆a
se insereze media aritmetic ̆a ˆıntre elementele de pe fiecare dou ̆a pozit, ii
consecutive.
Exemplu: Pentru lista 1 2 3 4 se vor insera mediile. Apelarea funct, iei
standard de afis, are a listei init, iale produce acum 1 1.5 2 2.5 3 3.5 4,
alternativ 1 1 2 2 3 3 4 dac ̆a lista e pe ˆıntregi.
 */

struct Node {
	Node *prev;
	int val;
	Node *next;
};
struct Node *head;

void adaugare(Node *start, int valoare) {
	Node *p = start;
	while (p->next) {
		p = p->next;
	}
	p->next = new Node();
	p->next->prev = p;
	p = p->next;
	p->val = valoare;
}

int list_length(Node *start) {
	Node *p = start;
	int counter = 0;
	while (p) {
		++counter;
		p = p->next;
	}
	return counter;
}

void inserat(Node *start, int valoare, int index) {
	int i = 0, n = list_length(start);
	Node *p = start;
	if (index == 0) {
		Node* q = new Node();
		q->val = valoare;
		q->next = head;
		head->prev = q;
		head = q;
		return;
	} else if (index == n) {
		adaugare(start, valoare);
		return;
	} else if (index < n) {
		while (i < index) {
			if (p->next) p = p->next;
			++i;
		}
	} else {
		cout << "Index " << index << " out of bounds.\n";
		return;
	}

	Node *q = new Node();
	q->val = valoare;
	q->prev = p->prev;
	q->next = p;
	p->prev->next = q;
	p->prev = q;
}

void afisare(Node *start) {
	Node *p = start;
	while (p) {
		cout << p->val << " ";
		p = p->next;
	}
	cout << endl;
}

void afisare_invers(Node *start) {
	Node *p = start;
	while (p->next) {
		p = p->next;
	}
	while (p) {
		cout << p->val << " ";
		p = p->prev;
	}
	cout << endl;
}

Node *cautare(Node *start, int valoare) {
	Node *p = start;
	int i = 0;
	while (p) {
		if (p->val == valoare) {
			return p;
		}
		p = p->next;
		++i;
	}
	if (p == nullptr) {
		return nullptr;
	}
}

void sterg_coada(Node *start) {
	Node *p = start->next;
	p->prev = nullptr;
	*start = *p;
}

void sterg_cap(Node *start) {
	Node *p = start;
	while (p->next->next) {
		p = p->next;
	}
	p->next = nullptr;
}

void sterg_index(Node *start, int index) {
	int i = 0;
	Node *p = start;
	while (i < index) {
		if (p->next) {
			p = p->next;
			++i;
		} else {
			cout << "Index " << index << " out of bounds.\n";
		}
	}
	if (i == 0) sterg_coada(start);
	else if (p->next == nullptr) sterg_cap(start);
	else {
		p->prev->next = p->next;
		p->next->prev = p->prev;
		p = nullptr;
	}
}

void sterg_valoare(Node *start, int valoare) {
	Node *p = cautare(start, valoare);
	if (p == nullptr) cout << "Valoarea nu a fost gasita.\n";
	if (p == start) {
		sterg_coada(start);
	} else if (p->next == nullptr) {
		sterg_cap(start);
	} else {
		p->prev->next = p->next;
		p->next->prev = p->prev;
		p = nullptr;
	}
}

int main() {
	int x, n, i = 0, nr_exercitiu = 1;
	head = new Node();
	cout << "Numarul de elemente: ";
	cin >> n;
	cout << "Numarul exercitiului: ";
	cin >> nr_exercitiu;

	if (nr_exercitiu == 1) {
		// Citesc lista
		cin >> x;
		++i;
		head->val = x;
		while (i < n) { // citesc i numere
			cin >> x;
			adaugare(head, x);
			++i;
		}
		cout << "Lista introdusa: ";
		afisare(head);

		i = 0; // parcurg index-ul cu i
		Node *p = head; // parcurg cu nodul p
		while (i < n - 1) { // merg pana la penultimul element
			int medie = (p->val + p->next->val) / 2;
			inserat(head, medie, i + 1);
			p = p->next->next;
			i += 2;
			++n;
		}
		cout << "Exercitiul 1: ";
		afisare(head);
	} else if (nr_exercitiu == 2) {
		Node* p;
		int j;
		while (i < n) { // citesc i numere
			j = 0; // cu j retin index-ul la care am ajuns cand parcurg lista
			p = head;
			cout << "Introduceti numarul: ";
			cin >> x;

			// adaug primul element
			if (i == 0) {
				p->val = x;
				++i;
				continue;
			}
			// parcurg lista si cand gasesc elementul il inserez (cazurile a si b din cerinta)
			while (p) {
				if (p->val >= x) {
					inserat(head, x, j);
					break;
				}
				p = p->next;
				++j;
			}
			// verific cazul c
			if (list_length(head) <= i) adaugare(head, x);
			++i;
		}
		afisare(head);
	} else if (nr_exercitiu == 3) {

	}


	return 0;
}
