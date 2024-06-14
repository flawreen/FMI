/*
 2 2
0 0
10 11
10 0
0 10
out: 20

#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int n, m;
vector<pair<int, int>> centrale, blocuri;
vector<int> d, viz;

int euclid(pair<int, int> x, pair<int, int> y) {
    return (x.first - y.first) * (x.first - y.first) + (x.second - y.second) * (x.second - y.second);
}

void init() {
    d.resize(m + 1);
    viz.resize(m + 1);
    fill(viz.begin(), viz.end(), 0);
    fill(d.begin(), d.end(), INT_MAX);
}


int main() {
    int x, y;
    cin >> n >> m;
    init();
    for (int i = 1; i <= n; ++i) {
        cin >> x >> y;
        centrale.emplace_back(x, y);
    }

    for (int i = 1; i <= m; ++i) {
        cin >> x >> y;
        blocuri.emplace_back(x, y);
    }

    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            d[i] = min(d[i], euclid(blocuri[i], centrale[j]));
        }
    }

    for (int i = 0; i < m; ++i) {
        int index = 0;
        int dd = INT_MAX;

        for (int j = 0; j < m; ++j)
            if (d[j] < dd && !viz[j]) {
                dd = d[j];
                index = j;
            }
        viz[index] = 1;
        for (int j = 0; j < m; ++j)
            if (!viz[j] && d[j] > euclid(blocuri[index], blocuri[j])) {
                d[j] = euclid(blocuri[index], blocuri[j]);
            }

    }

    long rez = 0;
    for (int i = 0; i < m; ++i) {
        rez += sqrt(d[i]);
    }
    cout << rez;
    return 0;
}
*/