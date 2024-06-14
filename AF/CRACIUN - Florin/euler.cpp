/*

#include <iostream>
#include <vector>
using namespace std;

int n, m;
vector<vector<int>> nodes;
vector<int> d;
vector<pair<int, int>> edges;
vector<int> ciclu;
vector<bool> del;

void init() {
    nodes.resize(n + 1);
    d.resize(n + 1);
    del.resize(m + 1);
    fill(nodes.begin(), nodes.end(), vector<int>());
    fill(del.begin(), del.end(), false);
    fill(d.begin(), d.end(), 0);
}

int find(int s) {
    // caut nod nesters
    while (!nodes[s].empty() && del[nodes[s].back()])
        nodes[s].pop_back();
    // nu mai are muchii
    if (nodes[s].empty()) return 0;

    int u = nodes[s].back();
    del[u] = true;
    // return la vecin
    return edges[u].first + edges[u].second - s;
}

void euler(int s) {
    while (int v = find(s))
        euler(v);
    ciclu.push_back(s);
}

int main() {
    int x, y;
    cin >> n >> m;
    init();

    while (m--) {
        cin >> x >> y;
        ++d[y];++d[x];
        edges.emplace_back(x, y);
        nodes[x].push_back(edges.size() - 1);
        nodes[y].push_back(edges.size() - 1);
    }

    for (const auto& x : d) {
        if (x % 2 != 0) {
            cout << -1;
            return 0;
        }
    }

    euler(1);
    for (const auto& u : ciclu) {
        cout << u << " ";
    }
    return 0;
}
*/