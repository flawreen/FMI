def det(P, Q, R):
    return Q[0] * R[1] + P[0] * Q[1] + R[0] * P[1] - Q[0] * P[1] - Q[1] * R[0] - R[1] * P[0]


def acoperire():
    n = int(input())
    puncte = []
    for i in range(n):
        puncte.append(tuple([int(x) for x in input().split()]))

    # Iau cel mai din stanga pct axa Ox
    pct_stg = puncte.index(min(puncte))
    puncte = puncte[pct_stg:] + puncte[:pct_stg]
    # Iau cel mai din dreapta pct axa Ox
    pct_dr = puncte.index(max(puncte))

    sol = [puncte[0]]
    for i in range(1, pct_dr+1):
        # Daca punctul curent nu e la stanga de ultimele 2 pct din sol modific solutia
        while len(sol) > 1 and det(sol[-2], sol[-1], puncte[i]) <= 0:
            sol.pop()
        sol.append(puncte[i])

    aux = [puncte[pct_dr]]
    puncte.append(puncte[0])
    for i in range(pct_dr + 1, len(puncte)):
        while len(aux) > 1 and det(aux[-2], aux[-1], puncte[i]) <= 0:
            aux.pop()
        aux.append(puncte[i])

    # Combin partea de sus cu partea de jos in afara de prima si ultima ca se repeta
    sol.extend(aux[1:-1])

    print(len(sol))
    for x in sol:
        print(f"{x[0]} {x[1]}")


acoperire()

