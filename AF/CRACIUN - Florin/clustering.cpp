/*

#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

struct Muchie {
    int i;  // index cuv 1
    int j;
    int cost;
};

int k;
vector<string> cuvinte;
vector<Muchie> muchii;
set<int> clase;
vector<int> frecv;
vector<int> tata;
vector<int> h;

void init(int n) {
    tata.resize(n + 1);
    h.resize(n + 1);
    frecv.resize(n + 1);
    fill(frecv.begin(), frecv.end(), 0);
    fill(tata.begin(), tata.end(), 0);
    fill(h.begin(), h.end(), 0);
}

bool sortMuchie(Muchie& a, Muchie& b) {
    return a.cost < b.cost;
}

int leven(string s1, string s2) {
    int m = s1.length(), n = s2.length();
    vector<vector<int>> mat(m + 1, vector<int>(n + 1, 0));

    for (int i = 1; i <= max(n, m); ++i) {
        if (i <= m) mat[i][0] = i;
        if (i <= n) mat[0][i] = i;
    }

    for (int i = 1;i <= m; ++i)
        for (int j = 1; j<= n; ++j) {
            if (s1[i-1] == s2[j-1])
                mat[i][j] = mat[i - 1][j - 1];
            else
                mat[i][j] = 1 + min(min(mat[i - 1][j], mat[i][j - 1]), mat[i - 1][j - 1]);
        }
    return mat[m][n];
}

int FindRepr(int x) {
    if (tata[x] == 0) {
        return x;
    }
    tata[x] = FindRepr(tata[x]);
    return tata[x];
}

void Union(int x, int y) {
    int rx = FindRepr(x), ry = FindRepr(y);
    if (h[rx] > h[ry]) {
        tata[ry] = rx;
    } else {
        tata[rx] = ry;
        if (h[rx] == h[ry]) {
            ++h[ry];
        }
    }
}

int grad_separare(int a, int n) {
    for (int i = a; i <= n; ++i)
        if (tata[muchii[i].i] != tata[muchii[i].j])
            return muchii[i].cost;
}

void kruskal(int n) {
    int nrmuchii = 0, nrpasi = 0;

    for (const auto& muchie : muchii) {
        if (nrmuchii == n - k) break;
        ++nrpasi;

        int p = FindRepr(muchie.i);
        int q = FindRepr(muchie.j);
        if (p != q) {
            Union(p, q);
            ++nrmuchii;
        }
    }

    for (int i = 1; i <= n; ++i) {
        FindRepr(i);
        if (tata[i] != 0) {
            clase.insert(tata[i]);
            frecv[i - 1] = tata[i];
        }
    }

    for (auto& c : clase) {
        for (int i = 0; i <= n; ++i) {
            if (frecv[i] == c) cout << cuvinte[i] << " ";
        }
        cout << endl;
    }

    cout << grad_separare(nrpasi, muchii.size()) << endl;
}

int main() {
    cin >> k;
    string cuv;
    int n;
    cin >> cuv;
    while (cuv != "-1") {
        cuvinte.push_back(cuv);
        cin >> cuv;
    }
    n = cuvinte.size();
    for (int i = 0; i < n-1; ++i) {
        for (int j = i + 1; j < n; ++j) {
            Muchie temp;
            temp.i = i + 1;
            temp.j = j + 1;
            temp.cost = leven(cuvinte[i], cuvinte[j]);
            muchii.push_back(temp);
        }
    }
    sort(muchii.begin(), muchii.end(), sortMuchie);

    init(n);

    kruskal(n);

    return 0;
}

 */