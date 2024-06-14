import sys
from enum import Enum


class Color(Enum):  # enum pt culori
    ALB = 1
    GRI = 2
    NEGRU = 3


with open("dfs.in", "r") as f:
    global graf, n, m
    n, m = [int(x) for x in f.readline().split()]
    graf: list[list[int]] = [list() for _ in range(n + 1)]
    for ls in f.readlines():
        ls = [int(x) for x in ls.split()]
        graf[ls[0]].append(ls[1])
        graf[ls[1]].append(ls[0])

print("\n".join([" ".join([str(x) for x in ls]) for ls in graf]))

sys.setrecursionlimit(n + 1)
color: list[Color] = [Color.ALB for _ in range(n + 1)]  # inlocuieste viz
desc: list[int] = [0 for _ in range(n + 1)]  # incepe descoperirea
fin: list[int] = [0 for _ in range(n + 1)]  # se termina descoperirea
tata: list[int] = [0 for _ in range(n + 1)]  # arbore df
timp: int = 0  # timp de explorare
ciclu = list()


def df(s):
    global timp, ciclu
    color[s] = Color.GRI  # intra in explorare
    timp += 1
    desc[s] = timp
    for neigh in graf[s]:
        if color[neigh] == Color.ALB:
            tata[neigh] = s
            # print(s, neigh, f"tata[{s}] = {tata[s]}", sep=" ")
            df(neigh)
        elif tata[s] != neigh:
            print(f"s: {s}")
            copy = s
            while copy != neigh:
                ciclu.append(copy)
                copy = tata[copy]
            ciclu.extend([s, neigh])
            return
    color[s] = Color.NEGRU  # iese din explorare
    timp += 1
    fin[s] = timp


df(1)
print(ciclu)

