//
// Created by flawreen on 6/1/23.
//

#include <iostream>
#include <vector>

using namespace std;

/*
 (2p) 3. Implementati o coada de prioritati (priority queue) folosind un heap.
 
Coada de prioritâti este formatã din elemente de tipul (valoare, prioritate).
Ea trebuie sã suporte extragerea elementului de prioritate cea mai im-portantà (unul dintre ele, pentru cã pot fi mai multe are au acecasi prioritate) si insertia unui element dupa prioritatea acestuia.
Intr-o implementare bazatà pe cozi (queue) vom obtine timp constant pentru extragerea elementalui de prioritate cea mai importantã (va fi primul in coada) si timp O(n) ca sa inseram un element in coada (pentru cã e ca la inserarea sortatà, trebuie insert sortat dupa prioritate, deci cautata pozitia sa).

 Când folosim un heap ambele operatii vor fi in timp O(log n). Implementati un min-heap sau max-heap dupa interpretarea dvs. a prioritâtii. De exemplu la unele sisteme de operare se foloses intregi pozitivi, unde cu cât este mai mic intregul respectiv asociat unui proces, cu atât acesta este mai important.
 */

// Am facut max-heap

void swap(int *a, int *b) {
	int temp = *b;
	*b = *a;
	*a = temp;
}

void heapify(vector<int> &v, int i) {
	int size = v.size();

	int maxx = i;
	int l = 2 * i + 1;
	int r = 2 * i + 2;
	if (l < size && v[l] > v[maxx])
		maxx = l;
	if (r < size && v[r] > v[maxx])
		maxx = r;

	if (maxx != i) {
		swap(&v[i], &v[maxx]);
		heapify(v, maxx);
	}
}

void insert(vector<int> &v, int newVal) {
	int size = v.size();
	if (size == 0) {
		v.push_back(newVal);
	} else {
		v.push_back(newVal);
		for (int i = size / 2 - 1; i >= 0; i--) { // de la jumatate in jos ca sa nu sortez frunze
			heapify(v, i);
		}
	}
}

void deleteNode(vector<int> &v, int val) {
	int size = v.size();
	int i;
	for (i = 0; i < size; i++) {
		if (val == v[i]) break;
	}
	swap(&v[i], &v[size - 1]);

	v.pop_back();
	for (int i = size / 2 - 1; i >= 0; i--) { // de la jumatate in jos ca sa nu sortez frunze
		heapify(v, i);
	}
}

int top(vector<int> &v) {
	return v[0];
}

void printt(vector<int> &v) {
	for (int i = 0; i < v.size(); ++i)
		cout << v[i] << " ";
	cout << "\n";
}

int main() {
	vector<int> heap;

	insert(heap, 3);
	insert(heap, 4);
	insert(heap, 9);
	insert(heap, 5);
	insert(heap, 2);

	printt(heap);
	cout << top(heap) << endl;
	deleteNode(heap, 4);
	printt(heap);
	deleteNode(heap, 9);
	printt(heap);
	cout << top(heap) << endl;
}

