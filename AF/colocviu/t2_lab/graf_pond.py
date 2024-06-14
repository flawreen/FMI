with open("grafpond.in", "r") as f:
    n, m = map(int, f.readline().split())
    graf = [[tuple()] for _ in range(n + 1)]
    for _ in range(m):
        i, j, k = map(int, f.readline().split())
        graf[i].append((j, k))
        graf[j].append((i, k))

print("\n".join([" ".join([str(x) for x in ls]) for ls in graf]))


