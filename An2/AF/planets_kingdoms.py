from sys import stdin, setrecursionlimit

setrecursionlimit(9999999)

input = stdin.readline
n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
gt = [[] for _ in range(n + 1)]
color = 1
viz = [0 for _ in range(n + 1)]
stk = []
for _ in range(m):
    i, j = map(int, input().split())
    g[i].append(j)
    gt[j].append(i)


def df(graf, s, transp=False):
    viz[s] = color
    for neigh in graf[s]:
        if not viz[neigh]:
            df(graf, neigh)
    if not transp:
        stk.append(s)


for i in range(1, n + 1):
    if not viz[i]:
        df(g, i)

viz = [0 for _ in range(n + 1)]
while stk:
    s = stk.pop()
    if not viz[s]:
        df(gt, s, True)
        color += 1

print(color - 1)
print(*viz[1:])
