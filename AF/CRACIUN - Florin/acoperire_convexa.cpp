#include <iostream>
#include <vector>
#include<string>
#include <cmath>
#include <climits>
using namespace std;

struct P {
    int x;
    int y;
};

#define pb push_back;
//int n, x_min = INT_MAX, pct_stg = 0;
vector<P> puncte;
vector<int> sol;

double dist(const P& p, const P& r) {
    return sqrt(pow(r.x - p.x, 2) + pow(r.y - p.y, 2));
}

int poz(const P& p, const P& q, const P& r) {
    return q.x * r.y + p.x * q.y + r.x * p.y - (q.x * p.y + q.y * r.x + p.x * r.y);
}


int main() {
    int p_curent, len_poligon = 0, p_next, n, x_min = INT_MAX, pct_stg = 0;
//    string res;
    cin >> n;
    if (n < 3) return 0;
    for (int i = 0; i < n; ++i) {
        P* temp = new P();
        cin >> temp->x >> temp->y;
        puncte.push_back(*temp);
        if (temp->x < x_min) {
            x_min = temp->x;
            pct_stg = i;
        }
        delete temp;
    }

    p_curent = pct_stg;

    while(1) {
        ++len_poligon;
        sol.push_back(p_curent);
//        res.append(to_string(puncte[p_curent].x));
//        res.append(" ");
//        res.append(to_string(puncte[p_curent].y));
//        res.append("\n");

        p_next = (p_curent + 1) % n;

        for (int i = 0; i < n; ++i)
            if (p_curent == p_next) {
                p_next = i;
            } else {
                int pos = poz(puncte[p_curent], puncte[p_next], puncte[i]);
                if (pos < 0 || (pos == 0 && dist(puncte[p_curent], puncte[i]) > dist(puncte[p_curent], puncte[p_next])))
                    p_next = i;
            }

        if (p_next != pct_stg) p_curent = p_next;
        else break;
    }

    cout << len_poligon << "\n";
    for (const auto& x : sol) {
        printf("%d %d\n", puncte[x].x, puncte[x].y);
    }

    return 0;
}

