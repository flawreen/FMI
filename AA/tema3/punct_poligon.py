def det(P, Q, R):
    return (Q[0] - P[0]) * (R[1] - P[1]) - (R[0] - P[0]) * (Q[1] - P[1])


def poz(d):
    if d > 0:
        return 1
    elif d < 0:
        return -1
    else:
        return 0


def rez(x):
    if x == 1:
        return "INSIDE"
    elif x == 0:
        return "BOUNDARY"
    elif x == -1:
        return "OUTSIDE"


def bin(PP, pct):
    st = 0
    dr = len(PP) - 1
    while st <= dr:
        mij = (st + dr) // 2
        if det(PP[0], PP[mij], pct) > 0:  # daca e la stanga
            st = mij + 1
        elif det(PP[0], PP[mij], pct) < 0:  # la dreapta
            dr = mij - 1
        else:
            return mij
    return dr


def afla_pozitia(pct):
    i = bin(PP, pct)
    if i == 0:
        return "OUTSIDE"

    if det(PP[i - 1], PP[i], pct) == 0:
        if (min(PP[i - 1][0], PP[i][0]) <= pct[0] <= max(PP[i - 1][0], PP[i][0]) and
                min(PP[i - 1][1], PP[i][1]) <= pct[1] <= max(PP[i - 1][1], PP[i][1])):
            return "BOUNDARY"

    if i == 1 or (i == len(PP)-1 and det(PP[i - 1], PP[i % len(PP)], pct) < 0):
        return "OUTSIDE"

    return rez(poz(det(PP[i], PP[(i + 1) % n], pct)))


freq = {}
PP = []
puncte = []

n = int(input())
for i in range(n):
    x, y = [int(xx) for xx in input().split()]
    PP.append([x, y])
    freq[(x, y)] = True

m = int(input())
puncte = [tuple([int(x) for x in input().split()]) for _ in range(m)]

for pct in puncte:
    if pct in freq.keys():
        print("BOUNDARY")
    else:
        print(afla_pozitia(pct))
