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
		Node *q = new Node();
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

//int swapNode( node *&head * &first, node * &second) {
//     node *firstprev=NULL;
//     node*secprev=NULL;
//     node*current=head;
//     while(current->next!=first)
//     {
//        current=current->next;
//     }
//     firstprev=current;
//     while(current->next!=second)
//     {
//        current=current->next;
//     }
//    int tempValue = first->value;
//    first->value = second->value;
//    second->value = tempValue;
//
//    firstprev->next=second;
//    secprev->next=first;
//


int main() {
	int x, n, i = 0, nr_exercitiu = 1;
	head = new Node();
	cout << "Numarul exercitiului: ";
	cin >> nr_exercitiu;

	// Exercitiul 1
	if (nr_exercitiu == 1) {
		// Citesc lista
		cout << "Numarul de elemente: ";
		cin >> n;
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
	}
		// Exercitiul 2
	else if (nr_exercitiu == 2) {
		cout << "Numarul de elemente: ";
		cin >> n;
		Node *p;
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
	}
		// Exercitiul 3 fara bonus
	else if (nr_exercitiu == 3) {
		cout << "Numarul de elemente: ";
		cin >> n;
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

		// Determin ultimul element din lista
		Node *end = head;
		Node *start = head;
		while (end->next != nullptr) end = end->next;

		Node *lista_inversata = new Node(); // Creez lista noua
		// Parcurg lista initiala de la final si adaug pe rand la lista_inversata
		lista_inversata->val = end->val;
		end = end->prev;
		while (end != nullptr) {
			adaugare(lista_inversata, end->val);
			end = end->prev;
		}

		cout << "Lista dupa inversare: ";
		afisare(lista_inversata);
	}
	// Exercitiul 4
	else if (nr_exercitiu == 4) {
		Node *lista1 = new Node();
		Node *lista2 = new Node();
		Node *lista3 = new Node();
		// Citesc prima lista
		cout << "Numarul de elemente lista 1: ";
		cin >> n;
		cin >> x;
		lista1->val = x;
		i = 1;
		while (i < n) {
			cin >> x;
			adaugare(lista1, x);
			++i;
		}
		// Citesc a doua lista
		cout << "Numarul de elemente lista 2: ";
		cin >> n;
		cin >> x;
		lista2->val = x;
		i = 1;
		while (i < n) {
			cin >> x;
			adaugare(lista2, x);
			++i;
		}
		cout << "Lista 1: ";
		afisare(lista1);
		cout << "Lista 2: ";
		afisare(lista2);
		// Incep interclasarea
		Node *p = lista1, *q = lista2;
		while (p != nullptr && q != nullptr) {
			if (p->val < q->val) {
				if (p == lista2) {
					lista3->val = p->val;
					p = p->next;
					continue;
				}
				adaugare(lista3, p->val);
				p = p->next;
			} else {
				if (q == lista2) {
					lista3->val = q->val;
					q = q->next;
					continue;
				}
				adaugare(lista3, q->val);
				q = q->next;
			}
		}
		while (p != nullptr) {
			adaugare(lista3, p->val);
			p = p->next;
		}
		while (q != nullptr) {
			adaugare(lista3, q->val);
			q = q->next;
		}

		cout << "Listele interclasate: ";
		afisare(lista3);
	}
	else if (nr_exercitiu == 5) {
		Node *lista1 = new Node();
		Node *lista2 = new Node();
		Node *lista3 = new Node();
		// Citesc prima lista
		cout << "Numarul de cifre pentru primul numar: ";
		cin >> n;
		cin >> x;
		lista1->val = x;
		i = 1;
		while (i < n) {
			cin >> x;
			adaugare(lista1, x);
			++i;
		}
		// Citesc a doua lista
		cout << "Numarul de cifre pentru al doilea numar: ";
		cin >> n;
		cin >> x;
		lista2->val = x;
		i = 1;
		while (i < n) {
			cin >> x;
			adaugare(lista2, x);
			++i;
		}
		cout << "Numarul 1: ";
		afisare(lista1);
		cout << "Numarul 2: ";
		afisare(lista2);
		// Incep suma
		Node *p = lista1, *q = lista2;
		int transport = 0, suma;
		while (p != nullptr && q != nullptr) {
			suma = p->val + q->val;
			p = p->next;
			q = q->next;
			if (transport > 0) {
				suma += transport;
				transport = 0;
			}
			if (suma > 9) {
				++transport;
				suma %= 10;
			}
			adaugare(lista3, suma);
		}
		while (p != nullptr) {
			suma = p->val;
			p = p->next;
			if (transport > 0) {
				suma += transport;
				transport = 0;
			}
			if (suma > 9) {
				++transport;
				suma %= 10;
			}
			adaugare(lista3, suma);
		}
		while (q != nullptr) {
			suma = q->val;
			q = q->next;
			if (transport > 0) {
				suma += transport;
				transport = 0;
			}
			if (suma > 9) {
				++transport;
				suma %= 10;
			}
			adaugare(lista3, suma);
		}
		if (transport > 0) {
			adaugare(lista3, transport);
		}
		sterg_coada(lista3);
		afisare_invers(lista3);
	}

	/*
	Exemplu1: 542 + 34 = 576 sau (2 → 4 → 5) + (4 → 3) = (6 → 7 → 5)
	Exemplu2: 19 + 11 = 30 sau (9 → 1) + (1 → 1) = (0 → 3)
	Exemplu3: 999 + 1 = 1000 sau (9 → 9 → 9) + (1) = (0 → 0 → 0 → 1)
	 */

	return 0;
}
