from sys import stdin
from collections import deque

input = stdin.readline
n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
d = [0 for _ in range(n+1)]
q = deque()
for _ in range(m):
    x, y = map(int, input().split())
    g[x].append(y)
    d[y] += 1

r = []
for i in range(1, n+1):
    if not d[i]:
        q.append(i)
while q:
    s = q.popleft()
    r.append(s)
    for v in g[s]:
        d[v] -= 1
        if not d[v]:
            q.append(v)

if len(r) != n:
    print("IMPOSSIBLE")
else:
    print(*r)
