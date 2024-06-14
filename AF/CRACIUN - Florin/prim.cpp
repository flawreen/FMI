/*

#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int n, m, l, s;
vector<int> stations, d, tata, viz;
vector<vector<pair<int, int>>> graf;
priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> q;

void init() {
    d.resize(n + 1);
    tata.resize(n + 1);
    viz.resize(n + 1);
    graf.resize(n + 1);
    fill(viz.begin(), viz.end(), 0);
    fill(tata.begin(), tata.end(), 0);
    fill(d.begin(), d.end(), INT_MAX);
}

long long prim() {
    long long sol = 0;
    while (!q.empty()) {
        int u = q.top().second;
        q.pop();
        if (viz[u]) continue;
        viz[u] = 1;
        sol += d[u];

        for (const auto& uv : graf[u]) {
            int v = uv.first;
            int w = uv.second;
            if (!viz[v] && w < d[v]) {
                d[v] = w;
                q.emplace(d[v], v);
            }
        }
    }

    return sol;
}

int main() {
    int x, y, z;
    cin >> n >> m >> l >> s;
    init();
    for (int i = 1; i <= s; ++i) {
        cin >> z;
        stations.push_back(z);
        d[z] = 0;
        q.emplace(d[z], z);
    }

    for (int i = 1; i <= m; ++i) {
        cin >> x >> y >> z;
        graf[x].emplace_back(y, z);
        graf[y].emplace_back(x, z);
    }

    long long sol = prim() + (n - s) * l;

    cout << sol;
    return 0;
}

 */