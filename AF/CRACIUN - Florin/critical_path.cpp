/*
    Drum critic (Critical Path Method). Se citesc din fișierul activitati.in următoarele informații despre activitățile care trebuie să se desfășoare în cadrul unui proiect:

    n – numărul de activități (activitățile sunt numerotate 1,…, n)

    d1, d2, …., dn durata fiecărei activități

    m – număr natural

    m perechi (i, j) cu semnificația: activitatea i trebuie să se încheie înainte să înceapă j

Activitățile se pot desfășura și în paralel.

Să se determine timpul minim de finalizare a proiectului, știind că acesta începe la ora 0 (echivalent – să se determine durata proiectului) și o succesiune (critică) de activități care determină durata proiectului (un drum critic – v. curs) O(m + n).

Să se afișeze pentru fiecare activitate un interval posibil de desfășurare (!știind că activitățile se pot desfășura în paralel) O(m + n).

6
7 4 30 12 2 5
6
1 2
2 3
3 6
4 3
2 6
3 5
Timp minim:47
Activitati critice: 4 3 6
1: 0 7
2: 7 11
3: 12 42
4: 0 12
5: 42 44
6: 42 47
#include <iostream>
#include <vector>
#include <stack>
using namespace std;

int n, m;
vector<int> d, g, tata, viz;
vector<vector<int>> nodes;
stack<int> stk;

void init() {
    g.resize(n + 1);
    tata.resize(n + 1);
    nodes.resize(n + 1);
    fill(g.begin(), g.end(), 0);
    fill(tata.begin(), tata.end(), 0);
    d.push_back(0);
}

void drum(int x) {
    if (tata[x] != 0) drum(tata[x]);
    cout << x << " ";
}

void dfs(int x) {
    viz[x] = 1;
    for (const auto& v : nodes[x]) {
        if (!viz[v])
            dfs(v);
    }
    stk.push(x);
}

void sortTop() {
    viz = vector<int>(n + 1, 0);
    for (int i = 1; i <= n; ++i)
        if (!viz[i])
            dfs(i);
}


int main() {
    int x, y;
    cin >> n;
    init();
    for (int i = 1; i <= n; ++i) {
        cin >> x;
        d.push_back(x);
    }
    cin >> m;
    for (int i = 1; i <= m; ++i) {
        cin >> x >> y;
        nodes[x].push_back(y);
    }

    sortTop();

    viz = vector<int>(n + 1, 0);
    while (!stk.empty()) {
        int u = stk.top();
        stk.pop();
        for (const auto& v : nodes[u])
            if (g[v] < g[u] + d[u]) {
                g[v] = g[u] + d[u];
                tata[v] = u;
            }
    }

    int i_min = 0, minim = 0;
    for (int i = 1; i <= n; ++i) {
        if (g[i] + d[i] > minim) {
            i_min = i;
            minim = g[i];
        }
    }
    cout << "Timp minim:" << g[i_min] + d[i_min] << endl;
    cout << "Activitati critice: ";
    drum(i_min);
    cout << endl;
    for (int i = 1; i <= n; ++i) {
        cout << i << ": " << g[i] << " " << d[i] + g[i] << endl;
    }

    return 0;
}

 */