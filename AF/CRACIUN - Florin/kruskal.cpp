/*


#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

int n, m, k, B, h[100001] = { 0 }, tata[100001];

struct Muchie {
    int x;
    int y;
    long long k;
    bool viz;
};
vector<Muchie> graf;
vector<Muchie> solutie;

bool sortMuchie(Muchie& a, Muchie& b) {
    if (a.k != b.k) return a.k < b.k;
    else {
        return a.x < b.x;
    }
}

void printMuchie(Muchie& x) {
    cout << x.x << " " << x.y << " " << x.k << " vizitata: " << x.viz << endl;
}

int FindRepr(int x) {
    if (tata[x] == -1) {
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


int main() {
    int a, b, c, nrmuchii = 0, p, q;
    long long sol = 0;
    cin >> n >> m >> k >> B;
    if (k > n) {
        cout << "Nu";
        return 0;
    }

    for (int i = 0; i <= n; ++i) {
        tata[i] = -1;
    }

    Muchie temp;
    for (int i = 0; i < m; ++i) {
        cin >> a >> b >> c;
        temp.x = a;
        temp.y = b;
        temp.k = c;
        temp.viz = false;
        graf.push_back(temp);
    }

    sort(graf.begin(), graf.end(), sortMuchie);

    for (int i = 0; i < k; ++i) {
        cin >> a >> b;
        for (auto& uv : graf) {
            if (uv.x == a && uv.y == b) {
                uv.viz = true;
                ++nrmuchii;
                sol += uv.k;

                if (sol > B) {
                    cout << "Nu";
                    return 0;
                }

                p = FindRepr(uv.x);
                q = FindRepr(uv.y);
                if (p != q) Union(p, q);
                solutie.push_back(uv);
            }
        }
    }


//    for (auto x : graf) {
//        printMuchie(x);
//    }

    for (auto& uv : graf) {
        if (nrmuchii == n - 1)
            break;
        p = FindRepr(uv.x);
        q = FindRepr(uv.y);

        if (p != q && !uv.viz) {
            sol += uv.k;
            uv.viz = true;
            ++nrmuchii;
            Union(p, q);
            solutie.push_back(uv);
        }

        if (sol > B) {
            cout << "Nu";
            return 0;
        }

    }

    cout << "Da\n";
    for (auto x : solutie) {
        cout << x.x << " " << x.y << endl;
    }

    return 0;
}*/