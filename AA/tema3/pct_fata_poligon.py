def det(P, Q, R):
    return (Q[0] - P[0]) * (R[1] - P[1]) - (R[0] - P[0]) * (Q[1] - P[1])


def rez(x):
    if x == 1:
        return "INSIDE"
    elif x == 0:
        return "BOUNDARY"
    elif x == -1:
        return "OUTSIDE"


def pe_linie(P, Q, R):
    if det(P, Q, R) != 0:
        return 0
    if Q[0] != R[0]:
        return Q[0] <= P[0] <= R[0] or R[0] <= P[0] <= Q[0]
    return Q[1] <= P[1] <= R[1] or R[1] <= P[1] <= Q[1]


def intersectie(P, Q, R):
    if P[1] > Q[1] and P[1] > R[1]:
        return 0
    else:
        if P[1] <= Q[1] and P[1] <= R[1]:
            return 0
        else:
            return 1 if float((P[1] - Q[1]) * (R[0] - Q[0]) + Q[0] * (R[1] - Q[1])) / float(R[1] - Q[1]) >= P[0] else 0


def intersectie_puncte(pct):
    nr_inters = 0
    for i in range(n - 1):
        if pe_linie(pct, PP[i], PP[i + 1]):
            return "BOUNDARY"
        nr_inters += intersectie(pct, PP[i], PP[i + 1])

    if pe_linie(pct, PP[n - 1], PP[0]):
        return "BOUNDARY"

    nr_inters += intersectie(pct, PP[n - 1], PP[0])

    if nr_inters % 2 == 1:
        return "INSIDE"
    else:
        return "OUTSIDE"


PP = []
puncte = []

n = int(input())
for i in range(n):
    x, y = [int(xx) for xx in input().split()]
    PP.append([x, y])

m = int(input())
puncte = [[int(x) for x in input().split()] for _ in range(m)]

for pct in puncte:
    print(intersectie_puncte(pct))
    