import sys
from sys import stdin, setrecursionlimit

setrecursionlimit(99999999)

input = stdin.readline
color = 0
prevColor = 0
n, m = map(int, input().split())
graf = [[0] for _ in range(n + 1)]
for i in range(1, n + 1):
    graf[i].extend(list(map(lambda x: -1 if x == '.' else 0, *input().split())))  # dau unpack ca sa iau fiecare char


def inBounds(x, y):
    if 0 < x <= n and 0 < y <= m:
        return True
    return False


def printImage():
    print("\n".join([" ".join([f"{x:2}" for x in ls[1:]]) for ls in graf[1:]]))
    print()


printImage()


def fill(x, y):
    global color, prevColor

    if not inBounds(x, y) or graf[x][y] >= 0:
        return
    elif color == prevColor:
        color += 1

    graf[x][y] = color
    fill(x + 1, y)
    fill(x, y + 1)
    fill(x - 1, y)
    fill(x, y - 1)


for i in range(1, n + 1):
    for j in range(1, m + 1):
        if graf[i][j] == -1:
            fill(i, j)
            prevColor = color

print(color)
