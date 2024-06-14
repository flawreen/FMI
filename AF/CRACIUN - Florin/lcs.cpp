/*
 Se dau două șiruri de caractere, litere mici ale alfabetului englez. Să se afișeze cel mai
lung subșir comun al lor. O(n*m)

#include <iostream>
#include <vector>

using namespace std;

void lcs(string t, string s, int m, int n) {
    cout << s << " " << t << endl;
    vector<vector<int>> mat(n + 1, vector<int>(m + 1, 0));
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            if (s[i - 1] == t[j - 1]) {
                mat[i][j] = 1;
            } else {
                if (n <= m) mat[i][j] = mat[i-1][j];
                else mat[i][j] = mat[i][j-1];
            }
        }
    }

    // afisare matrice
    cout << "  ";
    for (int j = 1; j <= m; ++j)
        cout << t[j-1] << " ";
    cout << endl;
    for (int i = 1; i <= n; ++i) {
        cout << s[i-1] << " ";
        for (int j = 1; j <= m; ++j) {
            cout << mat[i][j] << " ";
        }
        cout << endl;
    }

    // rezultat
    if (n <= m)
        for (int j = 1; j <= m; ++j) {
            if (mat[n][j]) cout << t[j - 1];
        }
    else
        for (int i = 1; i <= n; ++i)
            if (mat[i][m]) cout << s[i-1];
}


int main() {
    lcs("aaabcdrr", "agahbdertr", 8, 10);

    return 0;
}
 */