"""
    Drum critic (Critical Path Method). Se citesc din fișierul activitati.in următoarele informații despre activitățile care trebuie să se desfășoare în cadrul unui proiect:

    n – numărul de activități (activitățile sunt numerotate 1,…, n)

    d1, d2, …., dn durata fiecărei activități

    m – număr natural

    m perechi (i, j) cu semnificația: activitatea i trebuie să se încheie înainte să înceapă j

Activitățile se pot desfășura și în paralel.

Să se determine timpul minim de finalizare a proiectului, știind că acesta începe la ora 0 (echivalent – să se determine durata proiectului) și o succesiune (critică) de activități care determină durata proiectului (un drum critic – v. curs) O(m + n).

Să se afișeze pentru fiecare activitate un interval posibil de desfășurare (!știind că activitățile se pot desfășura în paralel) O(m + n).

      activitati.in


iesire

6

7 4 30 12 2 5

6

1 2

2 3

3 6

4 3

2 6

3 5


Timp minim 47

Activitati critice: 4 3 6

1: 0 7

2: 7 11

3: 12 42

4: 0 12

5: 42 44

6: 42 47
"""

with open("activitati.in", "r") as f:
    n = int(f.readline())
    d = [0] + [int(x) for x in f.readline().split()]
    g = [0 for _ in range(n + 1)]
    tata = [0 for _ in range(n + 1)]
    m = int(f.readline())
    muchie = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y = map(int, f.readline().split())
        muchie[x].append(y)
    sol = []


def drum(x):
    if tata[x] != 0:
        drum(tata[x])
    print(x, end=" ")


def dfs(x, stack, viz):
    viz[x] = True
    for y in muchie[x]:
        if not viz[y]:
            dfs(y, stack, viz)
    stack.append(x)


def sortTop():
    stack = []
    viz = [False for _ in range(n + 1)]
    for x in range(1, n + 1):
        if not viz[x]:
            dfs(x, stack, viz)
    return stack


Q = sortTop()
viz = [False for _ in range(n + 1)]
# print(Q)
while Q:
    x = Q.pop()
    for y in muchie[x]:
        if g[y] < g[x] + d[x]:
            g[y] = g[x] + d[x]
            tata[y] = x

i_min = 0
minim = 0
for i in range(1, n + 1):
    if g[i] + d[i] > minim:
        i_min = i
        minim = g[i]

print(g[i_min] + d[i_min])
drum(i_min)
print()
for i in range(1, n + 1):
    print(f"{i}: {g[i]} {d[i] + g[i]}")
# print()
# print(d, g, tata, sep="\n")
