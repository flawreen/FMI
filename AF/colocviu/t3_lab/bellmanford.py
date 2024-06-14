from collections import deque

with open("bellmanford.in", "r") as f:
    n, m = map(int, f.readline().split())
    graf = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, f.readline().split())
        graf[a].append((b, c))
    s = int(f.readline().split()[0])

q = deque()
q.append(s)
inq = [False for _ in range(n + 1)]
inq[s] = True
d = [float('inf') for _ in range(n + 1)]
d[s] = 0
tata = [0 for _ in range(n + 1)]
lung = [0 for _ in range(n + 1)]


def bell():
    while q:
        u = q.popleft()
        inq[u] = False

        for v, w in graf[u]:
            if d[u] < float('inf') and d[u] + w < d[v]:
                d[v] = d[u] + w
                tata[v] = u
                if not inq[v]:
                    q.append(v)
                    inq[v] = True

                lung[v] = lung[u] + 1
                if lung[v] > n:
                    return v


def drum(i, rez):
    while i != s:
        rez.appendleft(i)
        i = drum(tata[i], rez)
    return i


k = bell()

if k:
    rez = deque()
    rez.appendleft(drum(k, rez))

    with open("bellmanford.out", "w") as g:
        g.write("Circuit de cost negativ:\n")
        g.write(" ".join(str(x) for x in rez))
else:
    with open("bellmanford.out", "w") as g:
        for i in range(1, n + 1):
            if i == s:
                continue
            rez = deque()
            rez.appendleft(drum(i, rez))
            g.write("Drum: ")
            g.write(" ".join([str(x) for x in rez]))
            g.write(f" Cost: {d[i]}\n")


