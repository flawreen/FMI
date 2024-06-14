/*
A game has n planets, connected by m teleporters.
 Two planets a and b belong to the same kingdom exactly when
 there is a route both from a to b and from b to a.
 Your task is to determine for each planet its kingdom.

5 6
1 2
2 3
3 1
3 4
4 5
5 4
out: 2
 1 1 1 2 2

#include <iostream>
#include <climits>
#include <queue>
#include <stack>
#include <deque>
#include <algorithm>
#include <cmath>
using namespace std;

int n, m, color = 1;

vector<vector<int>> nodes;
vector<vector<int>> tnodes;
vector<int> viz;
stack<int> stk;

void init() {
    viz.resize(n + 1);
    fill(viz.begin(), viz.end(), 0);
    nodes.resize(n + 1);
    tnodes.resize(n + 1);
}

void df(vector<vector<int>>& graf, int s) {
    viz[s] = color;
    for (const auto& v : graf[s])
        if (!viz[v]) df(graf, v);
    stk.push(s);
}

int main() {
    int x, y;
    cin >> n >> m;
    init();

    while (m--) {
        cin >> x >> y;
        nodes[x].push_back(y);
        tnodes[y].push_back(x);
    }

    for (int i = 1; i <= n; ++i)
        if (!viz[i]) df(nodes, i);

    viz = vector<int>(n + 1, 0);
    while (!stk.empty()) {
        int s = stk.top();
        stk.pop();
        if (!viz[s]) {
            df(tnodes, s);
            ++color;
        }
    }

    --color;
    cout << color << endl;
    for (int i = 1; i <= n; ++i)
        cout << viz[i] << " ";

    return 0;
}

*/