/*
 Vice City is built over a group of islands, with bridges connecting them.
 As anyone in Vice City knows, the biggest fear of vice-citiers is that
 some day the islands will submerge. The big problem with this is that
 once the islands submerge, some of the other islands could get disconnected.
 You have been hired by the mayor of Vice city to tell him how many islands,
 when submerged, will disconnect parts of Vice City. You should know that
 initially all the islands of the city are connected.

Input
The input will consist of a series of test cases. Each test case will start with
 the number N (1 ≤ N ≤ 10^4) of islands, and the number M of bridges (1 ≤ M ≤ 10^5).
 Following there will be M lines each describing a bridge. Each of these M lines will contain
 two integers Ui, Vi (1 ≤ Ui,Vi ≤ N), indicating that there is a bridge connecting islands Ui
 and Vi. The input ends with a case where N = M = 0.

Output
For each case on the input you must print a line indicating the number of islands that,
 when submerged, will disconnect parts of the city.
6 8
1 3
6 1
6 3
4 1
6 4
5 2
3 2
3 5

out: 1

#include <iostream>
#include <climits>
#include <queue>
#include <stack>
#include <deque>
#include <algorithm>
#include <cmath>
using namespace std;

int n, m, timp = 0, sol = 0;

vector<vector<int>> nodes;
vector<int> viz;
vector<int> low;
vector<int> disc;
vector<int> tata;

void init() {
    nodes.resize(n + 1);

    viz.resize(n + 1);
    fill(viz.begin(), viz.end(), 0);
    low.resize(n + 1);
    fill(low.begin(), low.end(), INT_MAX);
    disc.resize(n + 1);
    fill(disc.begin(), disc.end(), INT_MAX);
    tata.resize(n + 1);
    fill(tata.begin(), tata.end(), -1);
}


void df(int s) {
    int copii = 0;
    disc[s] = timp + 1;
    low[s] = timp + 1;
    ++timp;
    viz[s] = 1;
    for (const auto& v : nodes[s]) {
        if (!viz[v]) {
            tata[v] = s;
            ++copii;
            df(v);
            low[s] = min(low[s], low[v]);  // vad daca s-a descoperit mai devreme

            // daca s nu e radacina si are descoperirea mai mica decat low-ul copilului
            if (tata[s] != -1 && disc[s] <= low[v])
                ++sol;

            // daca e radacina si are mai multi copii
            if (tata[s] == -1 && copii > 1)
                ++sol;


        } else if (v != tata[s])  // daca s nu e copilul vecinului il actualizez
            low[s] = min(low[s], disc[v]);
    }
}

int main() {
    int x, y;
    cin >> n >> m;
    init();

    while (m--) {
        cin >> x >> y;
        nodes[x].push_back(y);
        nodes[y].push_back(x);
    }
    
    for (int i = 1; i <= n; ++i)
        if (!viz[i]) df(i);

    cout << sol;

    return 0;
}
 */