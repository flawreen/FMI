/*
#include <iostream>
#include <queue>
#include <stack>
#include <algorithm>
using namespace std;

int n, m, k, s, t;
vector<int> tata;
vector<vector<int>> nodes; // lista de adiacenta
vector<vector<int>> flow; // matrice de flux
vector<vector<int>> invFlow;
vector<vector<int>> cap; // matrice de capacitate


void init(const int& nr) {
    nodes.resize(nr + 1);
    tata.resize(nr + 1);
    fill(tata.begin(), tata.end(), 0);
    flow.resize(nr + 1);
    invFlow.resize(nr + 1);
    cap.resize(nr + 1);
    fill(flow.begin(), flow.end(), vector<int>(n + 1, 0));
    fill(invFlow.begin(), invFlow.end(), vector<int>(n + 1, 0));
    fill(cap.begin(), cap.end(), vector<int>(n + 1, 0));
//    for (int i = 1; i <= n; ++i) {
//        flow[i] = vector<int>(n + 1, 0);
//        cap[i] = vector<int>(n + 1, 0);
//    }
}

// bf s-t pe graf rezidual
int bf() {
    vector<bool> viz(n + 1, false);
    queue<int> q;
    q.emplace(s);
    viz[s] = true;

    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int v = 1; v <= n; ++v) {
            if (!viz[v] && u != v && (cap[u][v] - flow[u][v] > 0 || invFlow[u][v] < 0)) {
                viz[v] = true;
                q.emplace(v);
                tata[v] = u;
                if (v == t) return 1;
            }
        }
    }
    return 0;
}

void ek() {
    int u, v;
    // flow nul initial

    while(bf()) {
        int pathFlow = INT_MAX;
        // det cost minim pe drum
        v = t;
        while (tata[v]) {
            u = tata[v];
            if (cap[u][v] - flow[u][v] > 0) pathFlow = min(pathFlow, cap[u][v] - flow[u][v]);
            else pathFlow = min(pathFlow, -invFlow[u][v]);
            v = u;
        }

        // actualizez graful rezidual
        v = t;
        while (tata[v]) {
            u = tata[v];
            if (cap[u][v] - flow[u][v] > 0) {
                flow[u][v] += pathFlow;
                invFlow[v][u] -= pathFlow;
            } else {
                flow[v][u] -= pathFlow;
                invFlow[u][v] += pathFlow;
            }
            v = u;
        }
    }
}

void afis() {
    vector<bool> viz(n + 1, false);
    queue<int> q;
    int u;
    q.push(s);
    while (!q.empty()) {
        u = q.front();
        q.pop();

        for (int v = 1; v <= n; ++v) {
            if (cap[u][v]) {
                cout << u << " " << v << " " << flow[u][v] << endl;
                if(!viz[v]) {
                    q.push(v);
                    viz[v] = true;
                }
            }
        }
    }
}


int taietura() {
    int capacitateTaietura = 0;
    vector<bool> viz(n + 1, false);
    queue<int> q;
    int u;
    q.push(s);
    while (!q.empty()) {
        u = q.front();
        q.pop();

        for (int v = 1; v <= n; ++v) {
            if (cap[u][v]) {
                if (cap[u][v] == flow[u][v]) {
                    cout << u << " " << v << endl;
                    capacitateTaietura += flow[u][v];
                }
                else q.push(v);
            }
        }
    }
    return capacitateTaietura;
}

void afisare() {
    cout << "DA\n";
    int flux = 0;
    for (int i = 1; i <= n; ++i)
        flux += flow[s][i];
    cout << flux << endl;
    afis();
    cout << taietura();
}

int main() {
    int x, y, z, c;
    cin >> n >> m;
    init(n);

    while(m--) {
        cin >> x >> y >> z >> c;
        nodes[x].emplace_back(y);
        cap[x][y] = z;
        flow[x][y] = c;
        invFlow[y][x] = -c;
    }

//    for (int i = 1; i <= n; ++i) {
//        for (int j = 1; j <= n; ++j)
//            cout << flow[i][j] << " " << cap[i][j] << "| ";
//        cout << endl;
//    }
//
//    for (const auto& u: nodes) {
//        for (const auto &v: u)
//            cout << v << " ";
//        cout << endl;
//    }

    ek();
    afisare();

    return 0;
}
*/