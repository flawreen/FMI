from collections import deque


def init():
    global aux
    with open("apm2.in", "r") as f:
        n, m, q = map(int, f.readline().split())
        graf = []

        for i in range(m):
            x, y, c = map(int, f.readline().split())
            graf.append([x, y, c])

        graf.sort(key=lambda x: x[2])
        aux = deque()

        aux.extend([list(map(int, f.readline().split())) for _ in range(q)])

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
    nrmuchii = 0
    nrpasi = 0
    h, tata = [0 for _ in range(n + 1)], [0 for _ in range(n + 1)]

    for muchie in muchii:
        if nrmuchii == n - 1:
            break
        nrpasi += 1
        p = FindRepr(muchie[0], tata)
        q = FindRepr(muchie[1], tata)
        if p != q:
            Union(p, q, tata, h)
            nrmuchii += 1

    with open("apm2.out", "w") as f:
        while aux:
            x, y = aux.popleft()
            for m in reversed(muchii):
                if x in m and tata[x] in m:
                    f.write(f"{m[2] - 1}\n")
                    break


init()
