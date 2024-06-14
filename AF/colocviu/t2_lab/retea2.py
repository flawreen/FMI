import math

with open("retea2.in", "r") as f:
    n, m = [int(x) for x in f.readline().split()]
    centrale = [tuple([int(x) for x in f.readline().split()]) for _ in range(n)]
    blocuri = [tuple([int(x) for x in f.readline().split()]) for _ in range(m)]

euclid = lambda x, y: (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2

dist = [1e6 + 1 for _ in range(m)]
for i in range(m):
    for j in range(n):
        dist[i] = min(dist[i], euclid(blocuri[i], centrale[j]))
viz = [False for _ in range(m)]

for i in range(m):
    index = 0
    d = 1e6 + 1
    for j in range(m):
        if dist[j] < d and not viz[j]:
            d = dist[j]
            index = j

    viz[index] = True
    for j in range(m):
        dist[j] = euclid(blocuri[index], blocuri[j]) if not viz[j] and dist[j] > euclid(blocuri[index], blocuri[j]) else \
        dist[j]

cost = sum(map(math.sqrt, dist))

with open("retea2.out", "w") as f:
    f.write(f"{cost:.6f}")
