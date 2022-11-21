"""
5. Se citesc de la tastatură două numere naturale n și m.
a) Să se scrie în fișierul matrice.in o matrice cu n linii și m coloane cu elemente mai mici
decât 100 generate aleator (fără a o memora). Exemplu de generare a unui număr mai mic
decât 100:
random.randrange(1,100)
"""
from random import randrange
n, m = randrange(3, 5), randrange(4, 6)
f = open("files/matrice.in", "w")
f.write("\n".join([" ".join([f"{randrange(1, 100):3}" for _ in range(m)]) for _ in range(n)]))
f.close()
"""
b) Se citește din fișierul matrice.in matricea generata la a). Să se genereze în memorie și
să se scrie în fișierul matrice.out transpusa matricei și matricea obținută din matricea
inițială ordonând crescător elementele de pe ultima coloana prin interschimbări de linii.
"""
f = open("files/matrice.in", "r")
mat = [[int(x) for x in linie.split()] for linie in f]
f.close()

transp = [[mat[i][j] for i in range(n)] for j in range(m)]
mat.sort(key=lambda m: m[-1])

g = open("files/matrice.out", "w")
g.write("\n".join([" ".join([f"{x:3}" for x in linie]) for linie in transp]))
g.write("\n\n")
g.write("\n".join([" ".join([f"{x:3}" for x in linie]) for linie in mat]))
g.close()


