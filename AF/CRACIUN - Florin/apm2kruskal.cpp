/*
Glorioasa Republică Populară va beneficia de un nou sistem de drumuri! Comisia prezidenţială desemnată sa realizeze această glorioasă sarcină a finalizat planul lucrărilor, folosindu-se cu talent de hârtia şi creioanele puse la dispoziţie de Republică pentru fiecare cetăţean. După cum ştie toată lumea, Republica are N mari oraşe, iar acestea vor fi legate de M drumuri bidirecţionale, fiecare astfel de drum având asociat o anumită taxă necesară pentru parcurgerea sa. Fiind dedicaţi omului de rând, membrii comisiei au aflat şi un arbore parţial de cost minim asociat noii reţele de drumuri, sugerând astfel o serie de drumuri ieftine pe care cetăţeanul le poate folosi pentru a călători intre oricare două oraşe ale Republicii.

Însă Marele Lider are alte priorităţi. Marele Fiu este un mare fan al emisiunii Top Gear, iar Marele Lider doreşte ca noua reţea de drumuri să-i impresioneze pe realizatorii acesteia, în caz că aceştia vor decide să viziteze ţara noastră. Astfel, Marele Lider desenează Q noi drumuri pe planul reţelei, drumuri care, după înţelepciunea sa, străbat peisaje impresionante. Marele Lider ar dori ca unul din aceste drumuri noi desenate să ajungă în construcţia finală. Dornici să îndeplinească dorinţa Luminatului Conducător, membrii comisiei se întreabă acum, pentru fiecare nou drum propus, care este cea mai mare taxă posibila pe care o pot asocia drumului respectiv astfel încât acesta să apară sigur în arborele parţial de cost minim al Republicii.
Date de intrare

Fisierul de intrare apm2.in va conţine pe prima sa linie cele trei numere N, M, şi Q. Fiecare dintre următoarele M linii va descrie câte un drum prin trei numere întregi: X, Y, cele două oraşe legate de drumul respectiv şi T, taxa asociată acestuia. Fiecare dintre următoarele Q linii va descrie câte un drum adăugat de Marele Lider, prin două numere, A şi B reprezentând cele două oraşe legate de drumul respectiv.
Date de ieşire

Fişierul de ieşire apm2.out va conţine Q linii. Pe a i-a linie se va afla răspunsul întrebarea 'Care este cea mai mare taxă pe care o putem asocia celei de a i-a muchii ipotetice astfel încât aceasta să se afle sigur în arborele parţial de cost minim al reţelei?'.

4 3 2
1 2 7
1 3 2
1 4 1
2 3
3 4
 out:
1
6
#include <iostream>
#include <deque>
#include <algorithm>
#include <vector>
using namespace std;

struct Muchie {
    int i;
    int j;
    int cost;
};

bool sortMuchie(Muchie& x, Muchie& y) {
    return x.cost < y.cost;
}

int n, m, q;
vector<Muchie> edges;
deque<pair<int, int>> aux;
vector<int> h, tata;

void init() {
    h.resize(n + 1);
    tata.resize(n + 1);
    fill(h.begin(), h.end(), 0);
    fill(tata.begin(), tata.end(), 0);
}

int FindRepr(int x) {
    if (tata[x] == 0) {
        return x;
    }
    tata[x] = FindRepr(tata[x]);
    return tata[x];
}

void Union(int x, int y) {
    int ry = FindRepr(x), rx = FindRepr(y);
    if (h[rx] > h[ry]) {
        tata[ry] = rx;
    } else {
        tata[rx] = ry;
        if (h[rx] == h[ry]) {
            ++h[ry];
        }
    }
}

void kruskal() {
    int nrmuchii = 0, nrpasi = 0;

    for (const auto& muchie : edges) {
        if (nrmuchii == n - 1) break;
        ++nrpasi;
        int p = FindRepr(muchie.i);
        int q = FindRepr(muchie.j);
        if (p != q) {
            Union(p, q);
            ++nrmuchii;
        }
    }

    while(!aux.empty()) {
        int x = aux.front().first;
        int y = aux.front().second;
        aux.pop_front();
        for (auto it = edges.begin(); it < edges.end(); it++) {
            if ((x == it->i || x == it->j) && (tata[x] == it->i || tata[x] == it->j)){
                cout << it->cost - 1 << endl;
                break;
            }
        }
    }

}


int main() {
    int x, y, z;
    cin >> n >> m >> q;

    init();

    for (int i = 0; i < m; ++i) {
        cin >> x >> y >> z;
        Muchie temp;
        temp.i = x;
        temp.j = y;
        temp.cost = z;
        edges.emplace_back(temp);
    }
    sort(edges.begin(), edges.end(), sortMuchie);

    for (int i = 0; i < q; ++i) {
        cin >> x >> y;
        aux.emplace_front(x, y);
    }

    kruskal();

    return 0;
}



 */