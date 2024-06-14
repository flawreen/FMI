from heapq import heappush, heapify, heappop


def init():
    global N, M, L, S, d, tata, g, q, viz
    datasets = int(input())
    while datasets > 0:
        datasets -= 1
        N, M, L, S = [int(x) for x in input().split()]
        stations = [int(x) for x in input().split()]
        d, tata = [int(1e6) + 1 for _ in range(N + 1)], [0 for _ in range(N + 1)]
        viz = [False for _ in range(N + 1)]
        g = [list() for _ in range(N + 1)]
        q = []
        for x in stations:
            d[x] = 0

        for _ in range(M):
            i, j, w = [int(x) for x in input().split()]
            g[i].append((j, w))
            g[j].append((i, w))
        for i in range(1, N + 1):
            heappush(q, [d[i], i])

        sol = prim() + (N - S) * L
        print(sol)


def heapupdate(i):
    for x in q:
        if x[1] == i:
            x[0] = d[i]
    heapify(q)


def prim():
    sol = 0
    while q:
        u = heappop(q)[1]
        viz[u] = True
        sol += d[u]
        for muchie in g[u]:
            if not viz[muchie[0]] and muchie[1] < d[muchie[0]]:
                d[muchie[0]] = muchie[1]
                tata[muchie[0]] = u
                heapupdate(muchie[0])

    return sol


init()
