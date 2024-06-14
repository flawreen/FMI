/*
You have to complete n courses. There are m requirements of the
 form "course a has to be completed before course b".
 Your task is to find an order in which you can complete the courses.

5 3
1 2
3 1
4 5

 out: 4 5 3 1 2

#include <iostream>
#include <vector>
#include <stack>
using namespace std;

int n, m, timp = 0;
stack<int> stk;
vector<int> viz;
vector<int> fin;
vector<vector<int>> nodes;

void init() {
    viz.resize(n + 1);
    fin.resize(n + 1);
    fill(viz.begin(), viz.end(), 0);
    fill(fin.begin(), fin.end(), 0);
    nodes.resize(n + 1);
}

void df(int s) {
    viz[s] = 1;

    timp += 1;
    for (const auto& v : nodes[s]) {
        if (!viz[v]) {
            df(v);
        }
    }
    timp += 1;
    fin[s] = timp;

    for (const auto& v : nodes[s])
        if (!fin[v]) {
            cout << "IMPOSSIBLE";
            exit(0);
        }

    stk.push(s);
}


int main() {
    int x, y;
    cin >> n >> m;
    init();
    while (m--) {
        cin >> x >> y;
        nodes[x].emplace_back(y);
    }

    for (int i = 1; i <= n; ++i)
        if (!viz[i]) {
            df(i);
        }

    while (!stk.empty()) {
        cout << stk.top() << " ";
        stk.pop();
    }

    return 0;
}

 */