"""
3. a) Scrieți o funcție care primește un număr întreg x și un număr variabil de liste nevide de
numere întregi și returnează numărul de liste primite ca parametru care conțin x.
Exemplu apel:
nr = liste_x(3, [1, 5, 7], [3], [1, 8, 3], [])
print(nr)
"""
def liste_x(x, *args):
    c = 0
    for ls in args:
        if x in ls:
            c += 1
    return c
nr = liste_x(3, [1, 5, 7], [3], [1, 8, 3], [])
print(nr)
"""
b) Modificați funcția de la a astfel încât rezultatul să nu fie returnat, ci să se salveze în
variabila globală rez. Exemplu apel:
rez = None
liste_x(3, [1, 5, 7], [3], [1, 8, 3], [4,3])
print(rez)
"""
def liste_x(x, *args):
    c = 0
    for ls in args:
        if x in ls:
            c += 1
    global rez
    rez = c
rez = None
liste_x(3, [1, 5, 7], [3], [1, 8, 3], [4, 3])
print(rez)

