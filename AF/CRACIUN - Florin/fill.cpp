/*
You are given a map of a building, and your task is to count the number of its rooms.
 The size of the map is n \times m squares, and each square is either floor or wall.
 You can walk left, right, up, and down through the floor squares.

5 8
########
#..#...#
####.#.#
#..#...#
########

out: 3


#include <iostream>
#include <vector>
#include <stack>
using namespace std;

int n, m, color = 0, prevColor = 0;
vector<vector<int>> nodes;

void init() {
    nodes.resize(n + 1);
    fill(nodes.begin(), nodes.end(), vector<int>(m + 1, 0));
}

bool inBounds(int x, int y) {
    if (x > 0 && x <= n && y > 0 && y <= m) return true;
    return false;
}

void fill(int x, int y) {
    if (!inBounds(x, y) || nodes[x][y] >= 0) return;
    else if (color == prevColor) ++color;

    nodes[x][y] = color;
    fill(x + 1, y);
    fill(x, y + 1);
    fill(x - 1, y);
    fill(x, y - 1);
}

int main() {
    char x;
    cin >> n >> m;
    init();
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            cin >> x;
            if (x == '.') nodes[i][j] = -1;
        }
    }

    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= m; ++j)
            if (nodes[i][j] == -1) {
                fill(i, j);
                prevColor = color;
            }

    cout << color;
    return 0;
}
 */