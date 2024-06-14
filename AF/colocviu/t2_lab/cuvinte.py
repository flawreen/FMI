from math import comb


def init():
    k = int(input("k = "))
    with open("cuvinte.in", "r") as f:
        cuvinte = [x for x in f.readline().split()]  # cuvintele se citesc de pe prima linie din fisier
        muchii = []

    # lista de muchii, o muchie e o lista de tip [cuvant1, cuvant2, cost(distanta levensthtein)]
    muchii = [[i + 1, j + 1, leven(cuvinte[i], cuvinte[j], muchii)] for i in range(len(cuvinte) - 1)
              for j in range(i + 1, len(cuvinte))]

    muchii.sort(key=lambda x: x[2])
    # if len(muchii) == comb(len(cuvinte), 2):
    #     print("OK")

    kruskal(len(cuvinte), muchii, k, cuvinte)


def leven(s1, s2, muchii):
    m, n = len(s1), len(s2)
    mat = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    # initializez matricea
    for i in range(1, max(n, m) + 1):
        if i <= m:
            mat[i][0] = i
        if i <= n:
            mat[0][i] = i

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            mat[i][j] = mat[i - 1][j - 1] if s1[i - 1] == s2[j - 1] else 1 + min(mat[i - 1][j], mat[i][j - 1], mat[i - 1][j - 1])

    return mat[m][n]


def Union(i, j, tata, h, cuvinte):
    r1, r2 = FindRepr(i, tata), FindRepr(j, tata)
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


def grad_separare(i, n, muchii, tata):  # plec cu i de la indexul muchiei la care s-a oprit kruskal
    for i in range(i, n + 1):
        if tata[muchii[i][0]] != tata[muchii[i][1]]:
            return muchii[i][2]


def kruskal(n, muchii, k, cuvinte):
    nrmuchii = 0
    nrpasi = 0
    h, tata = [0 for _ in range(n + 1)], [0 for _ in range(n + 1)]

    for muchie in muchii:
        if nrmuchii == n - k:
            break
        nrpasi += 1
        p = FindRepr(muchie[0], tata)
        q = FindRepr(muchie[1], tata)
        if p != q:
            Union(p, q, tata, h, cuvinte)
            nrmuchii += 1

    # fac un dictionar {index_reprezentant : [cuvinte]}
    clase = {}
    for i in range(1, n + 1):
        if tata[i] != 0:
            FindRepr(i, tata)
            if not clase.setdefault(tata[i], []):
                clase[tata[i]].append(cuvinte[tata[i] - 1])
            clase[tata[i]].append(cuvinte[i - 1])

    grad_sep = grad_separare(nrpasi, len(muchii), muchii, tata)

    # afisez rezultatul
    print("\n".join([" ".join([s for s in clase[x]]) for x in clase]), grad_sep, sep="\n")

    # print(tata, sep="\n")


init()
