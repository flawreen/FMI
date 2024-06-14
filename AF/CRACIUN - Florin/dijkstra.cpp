/*
#include <iostream>
#include <queue>
#include <stack>
#include <algorithm>
using namespace std;

int n, m, k, s;
vector<int> klist;
vector<long> d;
stack<int> res;
vector<int> tata;
vector<vector<pair<int, int>>> graf;
priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> q;

void init(const int& nr) {
    graf.resize(nr + 1);
    tata.resize(nr + 1);
    d.resize(nr + 1);

}

void dijkstra() {
    fill(tata.begin(), tata.end(), 0);
    fill(d.begin(), d.end(), INT_MAX);
    d[s] = 0;
    q.emplace(d[s], s);

    while (!q.empty()) {
        int u = q.top().second;
        q.pop();
        for (auto uv : graf[u]) {
            if (d[u] + uv.second < d[uv.first]) {
                d[uv.first] = d[u] + uv.second;
                q.emplace(d[uv.first], uv.first);
                tata[uv.first] = u;
            }
        }
    }
}

int drum(int i) {
    while (i != 0) {
        res.emplace(i);
        i = drum(tata[i]);
    }
    return i;
}


int main() {
    int x, y, z;
    cin >> n >> m;
    init(n);

    while(m--) {
        cin >> x >> y >> z;
        graf[x].emplace_back(make_pair(y, z));
        graf[y].emplace_back(make_pair(x, z));
    }


    cin >> k;
    while (k--) {
        cin >> x;
        klist.push_back(x);
    }
    cin >> s;

    dijkstra();
    int ii = klist[0];
    for (auto nr : klist) {
        if (d[nr] < d[ii])
            ii = nr;
    }

    cout << ii << endl;
    drum(ii);
    while (!res.empty()) {
        cout << res.top() << " ";
        res.pop();
    }

    return 0;
}
*/
