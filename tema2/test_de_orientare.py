t = int(input())


def det(P, Q, R):
    """
    Determinantul are forma:
    1  1  1
    p1 q1 r1
    p2 q2 r2
    """
    return Q[0] * R[1] + P[0] * Q[1] + R[0] * P[1] - (Q[0] * P[1] + Q[1] * R[0] + P[0] * R[1])


for _ in range(t):
    ls = [int(x) for x in input().split()]
    P, Q, R = (ls[0], ls[1]), (ls[2], ls[3]), (ls[4], ls[5])
    pos = det(P, Q, R)
    if pos == 0:
        print("TOUCH")
    elif pos < 0:
        print("RIGHT")
    else:
        print("LEFT")
