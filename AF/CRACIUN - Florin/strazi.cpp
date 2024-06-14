/*
#include <iostream>
#include <vector>
using namespace std;


int n, m, k, B, viz[100001] = { 0 }, culori[100001] = { 0 }, a, b, culoare = 1, rez[100001] = { 0 };
vector<int> graf[100001];




int main() {
    cin >> n >> m >> k;

    for (int i = 0; i < m; ++i) {
        cin >> a >> b;
        graf[a].push_back(b);
        graf[b].push_back(a);
    }

    for (int i = 1; i <= n; ++i) {
        if (!viz[i]) {
            df(i, viz, culori, culoare, graf);
        }
        ++culoare;
    }

    int i_max = 0;
    for (int i = 1; i <= n; ++i) {
        if (culori[i] > i_max) i_max = culori[i];
        ++rez[culori[i]];
    }

    int res = 0;
    for (int i = 1; i <= i_max; ++i) {
        if (rez[i] >= k) ++res;
    }

    cout << res;

    return 0;
}
*/