def init():
    n, m = map(int, input().split())
    graf = []

    for i in range(m):
        x, y, c = map(int, input().split())
        graf.append([x, y, c])

    graf.sort(key=lambda x: x[2])

    kruskal(n, graf)


def Union(i, j, tata, h):
    r2, r1 = FindRepr(i, tata), FindRepr(j, tata)
    if r1 > r2:
        tata[j] = i
    else:
        tata[i] = j
        if h[i] == h[j]:
            h[j] += 1


def FindRepr(i, tata):
    if tata[i] == 0:
        return i
    tata[i] = FindRepr(tata[i], tata)
    return tata[i]


def kruskal(n, muchii):
    global tata2
    nrmuchii, nrpasi, cost, cost2 = 0, 0, 0, 0
    h, tata = [0 for _ in range(n + 1)], [0 for _ in range(n + 1)]
    tata2 = []

    for muchie in muchii:
        if nrmuchii == n - 1:
            break
        nrpasi += 1
        p = FindRepr(muchie[0], tata)
        q = FindRepr(muchie[1], tata)
        if p != q:
            if nrmuchii == n - 2:
                tata2 = [x for x in tata]
                cost2 = 1 * cost
            Union(p, q, tata, h)
            cost += muchie[2]
            nrmuchii += 1
    print(cost, end=" ")

    for i in range(nrpasi, len(muchii)):
        p = FindRepr(muchii[i][0], tata2)
        q = FindRepr(muchii[i][1], tata2)
        if p != q:
            print(cost2 + muchii[i][2])
            break


init()
