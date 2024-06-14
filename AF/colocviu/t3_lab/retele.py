import heapq
from bisect import bisect_left

with open("retele.in", "r") as f:
    n, m = map(int, f.readline().split())
    tata = [0 for _ in range(n + 1)]
    graf = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, p = map(int, f.readline().split())
        graf[a].append((b, p))
    s, t = map(int, input().split())

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


def dijkstra():
    d = [float('inf') if i != s else 0 for i in range(n + 1)]  # initializez d
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
    return d


def drum(i, rez):
    while i != s:
        rez.append(i)
        i = drum(tata[i], rez)
    return i


dijkstra = dijkstra()
# print(dijkstra, tata, sep="\n")

rez = []
rez.append(drum(t, rez))
print(" ".join([str(x) for x in rez[::-1]]), f"cost: 2^(-{dijkstra[t]})")

