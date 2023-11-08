from sys import stdin
from collections import deque

input = stdin.readline
color = 0
q = deque()
n, m = map(int, input().split())
graf = [[0] for _ in range(n + 1)]
for i in range(1, n + 1):
    graf[i].extend(list(map(lambda x: -1 if x == '.' else 0, *input().split())))


def isValid(x, y):
    global color, graf, q
    if 0 < x <= n and 0 < y <= m and graf[x][y] == -1:
        graf[x][y] = color
        q.append((x, y))
        return True
    return False


def fill(x, y):
    global color
    isValid(x, y)

    while q:
        (x, y) = q.popleft()

        isValid(x + 1, y)
        isValid(x, y + 1)
        isValid(x - 1, y)
        isValid(x, y - 1)


for i in range(1, n + 1):
    for j in range(1, m + 1):
        if graf[i][j] == -1:
            fill(i, j)
            color += 1

print(color)
