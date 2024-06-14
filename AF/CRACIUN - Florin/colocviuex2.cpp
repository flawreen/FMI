/*

#include <iostream>
#include <vector>
#include <stack>
using namespace std;

int n, m, k;
vector<int> d, tata, viz;
vector<int> destinatii;
vector<vector<int>> nodes;
stack<int> stk;

void init() {
    tata.resize(n + 1);
    nodes.resize(n + 1);
    d.resize(n + 1);
    fill(d.begin(), d.end(), 0);
    fill(tata.begin(), tata.end(), 0);
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
    cin >> n >> m >> k;
    init();
    for (int i = 1; i <= k; ++i) {
        cin >> x;
        destinatii.push_back(x);
    }
    for (int i = 1; i <= m; ++i) {
        cin >> x >> y;
        nodes[x].push_back(y);
    }

    sortTop();

    viz = vector<int>(n + 1, 0);
    while (!stk.empty()) {
        int u = stk.top();
        stk.pop();
//        cout << u << endl;
        for (const auto& v : nodes[u]) {
//            cout << ": " << v << endl;
            if (d[u] >= d[v]) {
                d[v] = d[u] + 1;
                tata[v] = u;
            }
        }
    }
    int index_dest_max = destinatii[0];
    int val_dest_max = d[destinatii[0]];
    for (int i = 0; i < k; ++i) {
        int index = destinatii[i];
        if (d[index] > val_dest_max) {
            val_dest_max = d[index];
            index_dest_max = index;
        }
    }

//    for (int i = 1; i <= n; ++i) {
//        cout << tata[i] << " ";
//    }
//    cout << endl;

    cout << d[index_dest_max] << endl;
    drum(index_dest_max);


    return 0;
}

 */