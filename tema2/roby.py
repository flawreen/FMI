n = int(input())
P = [[int(x) for x in input().split()] for _ in range(n)]
st, dr, o = 0, 0, 0
P.append(P[0])


def det(P, Q, R):
    global st, dr, o
    """
    Determinantul are forma:
    1  1  1
    p1 q1 r1
    p2 q2 r2
    """
    pos = Q[0] * R[1] + P[0] * Q[1] + R[0] * P[1] - (Q[0] * P[1] + Q[1] * R[0] + P[0] * R[1])
    if pos == 0:
        o += 1
    elif pos < 0:
        dr += 1
    else:
        st += 1


for i in range(1, n):
    det(P[i-1], P[i], P[i+1])

print(st, dr, o)
