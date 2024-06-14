/*
There are n pupils in Uolevi's class, and m friendships between them.
 Your task is to divide the pupils into two teams in such a way that no two pupils
 in a team are friends. You can freely choose the sizes of the teams.

5 3
1 2
1 3
4 5

 out: 1 2 2 1 2


#include <iostream>
#include <vector>
#include <deque>
using namespace std;

int n, m;
vector<int> color;
vector<vector<int>> nodes;
deque<int> q;

void init() {
    color.resize(n + 1);
    nodes.resize(n + 1);
}

bool bf(int s) {
    if (color[s]) return true;

    q.push_back(s);
    color[s] = -1;

    while (!q.empty()) {
        s = q.front();
        q.pop_front();
        for (auto v : nodes[s]) {
            if (color[v] == color[s]) return false;
            else if (!color[v]) {
                q.push_back(v);
                color[v] = -color[s];
            }
        }
    }
    return true;
}


int main() {
    int x, y;
    cin >> n >> m;
    init();
    while (m--) {
        cin >> x >> y;
        nodes[x].emplace_back(y);
        nodes[y].emplace_back(x);
    }

    for (int i = 1; i <= n; ++i)
        if (!bf(i)) {
            cout << "IMPOSSIBLE";
            m = -1;
            return 0;
        }

    for (int i = 1; i <= n; ++i) {
        if (color[i] == 1) cout << 2 << " ";
        else cout << 1 << " ";
    }

    return 0;
}
 */