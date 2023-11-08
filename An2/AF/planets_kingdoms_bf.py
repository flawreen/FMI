from sys import stdin, setrecursionlimit
from collections import deque

setrecursionlimit(9999999)

input = stdin.readline
n, m = map(int, input().split())
g = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
gt = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
color = 1
viz = [0 for _ in range(n + 1)]
stk = []
for _ in range(m):
    i, j = map(int, input().split())
    g[i][j] = 1
    gt[j][i] = 1


def bf(graf, s, transp=False):
    q = deque()
    q.append(s)
    while q:
        s = q.popleft()
        if not transp and not viz[s]:
            stk.append(s)  # adaug in stiva pt graful transpus
        viz[s] = color
        for j in range(1, n + 1):
            if s != j and graf[s][j] and not viz[j]:
                q.append(j)


for i in range(1, n + 1):
    if not viz[i]:
        bf(g, i)
        
viz = [0 for _ in range(n + 1)]

while stk:
    s = stk.pop()
    if not viz[s]:
        bf(gt, s, True)
        color += 1

print(color-1)
print(*viz[1:])
