def det3(P, Q, R):
    return Q[0] * R[1] * P[2] + P[1] * Q[2] * R[0] + P[0] * Q[1] * R[2] - P[2] * Q[1] * R[0] - R[1] * Q[2] * P[0] - P[1] * Q[0] * R[2]


def det4(P, Q, R, S):
    det = 0
    mat = [[P[0], P[1], P[1]**2 + P[0]**2, 1],
        [Q[0], Q[1], Q[1]**2 + Q[0]**2, 1],
        [R[0], R[1], R[1]**2 + R[0]**2, 1],
        [S[0], S[1], S[1]**2 + S[0]**2, 1]]
    i = 0
    for j in range(4):
        coef = (-1)**(i+1+j+1) * mat[i][j]
        minor = []
        for k in range(1, 4):
            minor.append(mat[k][:j] + mat[k][j+1:])
        # print(minor)
        det += coef * det3(minor[0], minor[1], minor[2])
    return det


TT = [[int(x) for x in input().split()] for _ in range(4)]
# print(T, m, PP, sep="\n")
PP = [TT[3], TT[0]]
det1 = det4(TT[0], TT[1], TT[2], TT[3])  # triunghiul ABC
det2 = det4(TT[1], TT[2], TT[3], TT[0])  # triunghiul BCD
# print(det1, det2)
if det1 > 0:
    print("AC: ILLEGAL")
else:
    print("AC: LEGAL")

if det2 > 0:
    print("BD: ILLEGAL")
else:
    print("BD: LEGAL")



