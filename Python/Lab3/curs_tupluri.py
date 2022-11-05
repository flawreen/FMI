# metoda copy - copiere superficiala

ls = [[1, 2], [2, 3], 8]
ls1 = ls.copy()
ls[0][0] = 12
# print("1:", ls, ls1, sep="\n")
ls[2] = 7  # acum ls[2] va referi un alt obiect decat ls1[2]
# print("2:", ls, ls1, sep="\n")
ls[0] = [3, 4]  # va referi alt obiect decat ls1[0]
# print("3:", ls, ls1, sep="\n")

# +++ metoda deepcopy din modulul copy
import copy
ls1 = copy.deepcopy(ls)  # ls[0] si ls[1] NU mai refera acelasi obiect
ls[0][0] = 12
# print("4:", ls, ls1, sep="\n")
# si operatorii +, * fac copiere superficiala

# +++ TUPLURI
"""
clasa tuple
x, y = 1, 2
t = (3, 5) cu () in loc de []
"""
t = (3, 5)
print(t, type(t))
t = 3, 4
print(t, type(t))
t = (3, [2, 3])  # neomogene
print(t, type(t))
t = ()
print(t, type(t))
t = (2)  # nu este tuplu cu un singur element
print(t, type(t))
t = (2, )  # tuplu cu un singur element
print(t, type(t))

s = "o vocala"
print(s.startswith(tuple("aeiou")))  # tsteaza daca s incepe cu un element din tuplu
# comprehensiune - NU are
t = (1, 2)
# t[0] = 4 TypeError: 'tuple' does not support item assignment
# nu putem modifica catre ce obiect refera t[0]
t = ([5, 6], 2)
t[0][1] = 23  # pot modifica val ob referit de t[0], daca acesta e mutabil
print(t)

# UTILIZARE
# tuple assignment
x, y = 1, 2  # despachetare, nr de var stanga trebuie = lungime tuplu
x, *y = 1, 2, 3  # * - impachetare
print(x, y)

# +++ functii care returneaza mai multe valori
def f(x, y):
    return x+y, x*y
t = f(3, 5)
print(t, type(t))
s, p = f(3, 5)
print(s, p, type(s), type(p))
