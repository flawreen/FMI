//#include <iostream>
//#include <vector>
//#include <algorithm>
//
//using namespace std;
//
//int solution(int A, int B) {
//    if (A + B < 4) return 0;
//    // get the max and the min between the two numbers
//    int max = std::max(A, B), min = std::min(A, B);
//    // go from the max value down to 0 to find the first number x: A / x + B / x = 4
//    for (int i = max; i > 0; --i) {
//        if (max / i + min / i == 4) return i;
//    }
//    return 0;
//}
//
//int solution2(vector<int> &V, vector<int> &A, vector<int> &B) {
//    int M = B.size();
//    int C[100001] = { 0 };
//    for (int i = 0; i < M; ++i) {
//        ++C[B[i]];
//    }
//
//    int max1 = 0, max2 = 0;
//    for (int i = 0; i < V.size(); ++i) {
//        if (C[i] >= 2) continue;
//        if (V[i] > V[max1]) {
//            if (C[i] == 0) {
//                max2 = max1;
//                max1 = i;
//            } else {
//                for (int j = 0; j < M; ++j) {
//                    if (B[j] == i) {
//                        if (A[j] == max1) {
//                            max2 = max1;
//                            max1 = i;
//                        } else if (A[j] == max2) {
//                            max1 = max2;
//                            max2 = i;
//                        }
//                    }
//                }
//            }
//        } else if (V[i] > max2) {
//            if (C[i] == 0) {
//                max2 = i;
//            } else
//                for (int j = 0; j < M; ++j)
//                    if (B[j] == i && A[j] == max1) max2 = i;
//        }
//    }
//    return V[max1] + V[max2];
//}
//
//int main() {
//    vector<int> V = {-3, 5, 7, 2, 3};
//    vector<int> A = {3, 1};
//    vector<int> B = {2, 4};
//    cout << solution2(V, A, B);
//
//    return 0;
//}
