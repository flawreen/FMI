import sys

input = sys.stdin.readline
stk = list()
n, m = map(int, input().split())
graf = [[] for _ in range(n + 1)]
viz = [False for _ in range(n + 1)]
fin = [0 for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graf[x].append(y)
sys.setrecursionlimit(200001)
timp = 0


def df(s):
    global timp
    viz[s] = True
    timp += 1
    for neigh in graf[s]:
        if not viz[neigh]:
            df(neigh)
    timp += 1
    fin[s] = timp
    for neigh in graf[s]:
        if not fin[neigh]:
            print("IMPOSSIBLE")
            exit(0)
    stk.append(s)


for i in range(1, n + 1):
    if not viz[i]:
        df(i)
stk.reverse()
print(*stk)
