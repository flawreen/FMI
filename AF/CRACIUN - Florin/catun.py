import heapq
from bisect import bisect_left

with open("catun.in", "r") as f:
    n, m, k = map(int, f.readline().split())
    klist = [x for x in map(int, f.readline().split())]
    tata = [0 for _ in range(n + 1)]
    graf = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y, k = map(int, f.readline().split())
        graf[x].append((y, k))
        graf[y].append((x, k))


print("graf: ", "\n".join([" ".join([f"({ls[0]}, {ls[1]})" for ls in x]) for x in graf]))


def heapupdate(q, x, y, i):
    k = bisect_left(q, x, key=lambda x: x[0])  # bin search in heap dupa pondere

    j = k
    # caut doua pozitii in dreapta
    while j < len(q) - 1 and j - k < 2 and (q[j][0] != x or q[j][1] != i):
        j += 1

    if q[j][0] == x and q[j][1] == i:
        q[j][0] = y
        return

    j = k
    # caut doua pozitii in stanga
    while j >= 0 and k - j < 2 and (q[j][0] != x or q[j][1] != i):
        j -= 1

    q[j][0] = y


def drum(i):
    while tata[i] != 0:
        i = drum(tata[i])
    return i


def dijkstra():
    d = [float('inf') for _ in range(n + 1)]  # initializez d

    for nr in klist:
        d[nr] = 0

    q = [[d[i], i] for i in range(1, len(d))]
    heapq.heapify(q)
    while q:
        u = heapq.heappop(q)[1]
        for v, w in graf[u]:
            if d[u] + w < d[v]:
                new_val = d[u] + w
                heapupdate(q, d[v], new_val, v)
                heapq.heapify(q)
                d[v] = new_val
                tata[v] = u


dijkstra()

with open("catun.out", "w") as g:
    g.write(" ".join([str(x) for x in list(map(lambda x: drum(x) if x > 0 else 0, tata[1:]))]))

