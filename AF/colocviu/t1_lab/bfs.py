# import sys
from collections import deque

# class Color(Enum):  # enum pt culori
#     ALB = 1
#     GRI = 2
#     NEGRU = 3


with open("bfs.in", "r") as f:
    global graf, n, m, start
    n, m, start = [int(x) for x in f.readline().split()]
    graf = [list() for _ in range(n + 1)]
    for ls in f.readlines():
        ls = [int(x) for x in ls.split()]
        graf[ls[0]].append(ls[1])

# sys.setrecursionlimit(n * 2)
d = [-1 for _ in range(n + 1)]
viz = [False for _ in range(n + 1)]
q = deque()
d[start] = 0


def bf(s):
    viz[s] = True
    q.append(s)

    while len(q) > 0:
        x = q.popleft()
        for neigh in graf[x]:
            if neigh == x or viz[neigh]:
                continue
            viz[neigh] = True
            q.append(neigh)
            d[neigh] = d[x] + 1


bf(start)
with open("bfs.out", "w") as f:
    f.write(" ".join([str(d[i]) for i in range(1, n + 1)]))
