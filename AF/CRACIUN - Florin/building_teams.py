from collections import deque

n, m = [int(x) for x in input().split()]
color = [0 for _ in range(n + 1)]
graf = [list() for _ in range(n + 1)]
q = deque()
# citire graf
for _ in range(m):
    ls = [int(x) for x in input().split()]
    graf[ls[0]].append(ls[1])
    graf[ls[1]].append(ls[0])


def bf(s):
    if color[s]:
        return True

    q.append(s)
    color[s] = -1

    while q:
        s = q.popleft()
        for neigh in graf[s]:
            if color[neigh] == color[s]:
                return False
            elif not color[neigh]:
                q.append(neigh)
                color[neigh] = color[s] * -1
    return True


for i in range(n+1):
    if not bf(i):
        print("IMPOSSIBLE")
        m = -1
        break

if m != -1:
    print(" ".join([str(1) if color[i] == 1 else str(2) for i in range(1, n+1)]))

# pt fiecare nod verific daca exista un vecin cu aceeasi culoare (imposibil)
# in caz contrar e bipartit
# complexitate timp O(n+m), pt fiecare nod verific vecinii