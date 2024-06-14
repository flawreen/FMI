from sys import stdin, setrecursionlimit
setrecursionlimit(99999999)

input = stdin.readline
n, m = map(int, input().split())
sol = []


def df(s, p, graf, viz, low, disc, time):
    copii = 0  # nr de copii ce pornesc din s
    disc[s] = time
    low[s] = time
    time += 1

    for nei in graf[s]:
        if not viz[nei]:
            p[nei] = s
            copii += 1
            df(nei, p, graf, viz, low, disc, time)

            low[s] = min(low[s], low[nei])  # vad daca s e descoperit mai devreme

            # daca s nu e radacina si are descoperirea mai mica decat low-ul copilului
            if p[s] == -1 and disc[s] <= low[nei]:
                sol[-1] += 1

            if p[s] == 1 and copii > 1:  # daca e radacina si are mai multi copii
                sol[-1] += 1

        elif nei != p[s]:  # daca s nu e copilul vecinului il actualizez
            low[s] = min(low[s], disc[nei])


while n and m:
    g = [[] for _ in range(n + 1)]  # graful
    viz = [0 for _ in range(n + 1)]  # vizitari
    low = [float("Inf") for _ in range(n + 1)]  # timp min de descoperire
    disc = [float("Inf") for _ in range(n + 1)]  # cand a fost descoperit
    p = [-1 for _ in range(n + 1)]  # arbore df
    time = 0
    for _ in range(m):
        i, j = map(int, input().split())
        g[i].append(j)
        g[j].append(i)

    sol.append(0)
    for i in range(1, n + 1):
        if not viz[i]:
            df(i, p, g, viz, low, disc, time)

    n, m = map(int, input().split())

print("\n".join([str(x) for x in sol]))
