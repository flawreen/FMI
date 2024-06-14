from typing import List

with open("apm.in", "r") as f:
    n, m = map(int, f.readline().split())
    graf = []

    for i in range(m):
        x, y, c = map(int, f.readline().split())
        graf.append([x, y, c, 0])

    graf.sort(key=lambda x: x[2])

h = [0 for _ in range(n + 1)]
tata = [0 for _ in range(n + 1)]


def Union(x: int, y: int):
    rx, ry = FindRepr(x), FindRepr(y)
    if h[rx] > h[ry]:
        tata[ry] = rx
    else:
        tata[rx] = ry
        if h[rx] == h[ry]:
            h[ry] += 1


def FindRepr(x: int) -> int:
    if tata[x] == 0:
        return x
    tata[x] = FindRepr(tata[x])
    return tata[x]


s = 0
nrmuchii = 0
for i in range(m):
    if nrmuchii == n - 1:
        break
    p = FindRepr(graf[i][0])
    q = FindRepr(graf[i][1])

    if p != q:
        s += graf[i][2]
        graf[i][3] = 1
        nrmuchii += 1
        Union(p, q)

print(tata, h, sep="\n")

with open("apm.out", "w") as f:
    f.write(f"{s}\n{n - 1}\n")
    for i in range(m):
        if graf[i][3] == 1:
            f.write(f"{graf[i][0]} {graf[i][1]}\n")
