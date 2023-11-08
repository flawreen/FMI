from sys import setrecursionlimit

setrecursionlimit(99999999)

with open("graf.in", "r") as f:
    n, m = map(int, f.readline().split())
    g = [[] for _ in range(n + 1)]
    viz = [0 for _ in range(n + 1)]
    tata = [-1 for _ in range(n + 1)]

    for _ in range(m):
        i, j = map(int, f.readline().split())
        g[i].append(j)
        g[j].append(i)


def df(s):
    viz[s] = 1
    for nei in g[s]:
        if not viz[nei]:
            tata[nei] = s
            df(nei)


for i in range(1, n + 1):
    if not viz[i]:
        df(i)

for i in range(1, n + 1):
    print(i, tata[i])

