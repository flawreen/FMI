import heapq
from bisect import bisect_left

with open("grafpond.in", "r") as f:
    n, m = map(int, f.readline().split())
    tata = [0 for _ in range(n + 1)]
    graf = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y, k = map(int, f.readline().split())
        graf[x].append((y, k))
        graf[y].append((x, k))
    k = int(f.readline().split()[0])
    klist = [x for x in map(int, f.readline().split())]
    s = int(f.readline().split()[0])

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
    while i != 0:
        rez.append(i)
        i = drum(tata[i], rez)
    return i


dijkstra = dijkstra()
i_min = klist[-1]
for i in klist:
    if dijkstra[i] < dijkstra[i_min]:
        i_min = i


with open("grafpond.out", "w") as f:
    f.write(str(i_min))
    f.write("\n")
    rez = []
    drum(i_min, rez)
    f.write(" ".join([str(x) for x in rez[::-1]]))
