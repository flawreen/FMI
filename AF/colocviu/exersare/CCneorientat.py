from sys import setrecursionlimit
setrecursionlimit(100001)

n, m, k = [int(x) for x in input().split()]
graf = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = [int(x) for x in input().split()]
    graf[a].append(b)
    graf[b].append(a)

viz = [False for _ in range(n + 1)]
culori = [0 for _ in range(n + 1)]


def df(s, culoare):
    viz[s] = True
    culori[culoare] += 1
    for v in graf[s]:
        if not viz[v]:
            df(v, culoare)


culoare = 1
for i in range(1, n + 1):
    if not viz[i]:
        df(i, culoare)
    culoare += 1

rez = 0
for i in range(1, n + 1):
    if culori[i] >= k:
        rez += 1
print(rez)
