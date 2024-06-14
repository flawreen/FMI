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


T = [[int(x) for x in input().split()] for _ in range(3)]
m = int(input())
PP = [[int(x) for x in input().split()] for _ in range(m)]
# print(T, m, PP, sep="\n")

for pct in PP:
    det = det4(T[0], T[1], T[2], pct)
    if det == 0:
        print("BOUNDARY")
    elif det > 0:
        print("INSIDE")
    else:
        print("OUTSIDE")



