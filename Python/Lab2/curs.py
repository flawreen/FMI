"""
#  Interogari, cautari in secvente
#  operatorii in, not in
s = "un sir de caractere"
if "sir" not in s:
    print(f'{s} nu contine subsecventa "sir"')
else:
    print(f'"{s}" contine subsecventa "sir"')

#  Metoda Count
#  count(element_cautat, start, end) - start si end sunt optionali, ca la feliere
s = "acesta este un exemplu"
#  numara in felia s[start:end]
print(s.count("a"))  # in tot sirul
print(s.count("a", 1))  # incepand cu pozitia 1
print(s.count("a", 1, 5))

#  index(element, start, end)
#  pozitia primei operatii, daca elementul se afla in secventa
#  daca elementul nu se afla in structura =>  eroare

poz = s.index("a")  # primul index
print(poz)
poz = s.index("a", poz + 1)  # al doilea index
print(poz)

try:
#bloc de instructiuni
# Recomandare: cate o ramura pentru fiecare eroare cate un except -> except ValueError:
    poz = s.index("a", poz + 1)  # al treilea index
    print(poz)
except:
    print("nu apare de 3 ori")

# Exercitiu - toate pozitiile pe care apare in s un caracter dat
c = "a"
try:
    poz = s.index(c)
    while True:
        print(poz, end=" ")
        poz = s.index(c, poz+1)
except:
    pass
"""
"""
# Operatori relationali, +, *
# concatenare cu + => obiect nou, cu copierea operatorilor
s1 = "un"
s2 = "alt"
s = s1 + " " + s2

ls = [2, 3]
ls2 = [4, 5]
ls = ls + ls2 # obiect nou in care copiaza ls, ls2
# recomandare: pt a adauga elementele unei liste la alta lista, fol metoda extend (modifica ob curent)
ls.extend(ls2)
ls = [[1, 2], [4, 5]]
ls2 = [[5, 6]]
ls3 = ls + ls2 + ls
print(f' ls3: {ls3}')
ls3[0][0] = 130  # se va modifica si in ls3 si in ls, copierea se face la nivel de referinta, e mutabila
print(f' ls3: {ls3}')
print(f' ls3: {ls}')
# multiplicare cu * n
s = "ab" * 5
n = 3
ls = [0] * n
print(f'ls: {ls}')
ls[1] = 12
print(f'ls: {ls}')


# Operatori relationali <, <=, ...
ls = [4, 5]
ls2 = [1, 2, 3]
print(ls > ls2)  # il compara pe 4 cu 1 si deja iese ls mai mare
s = "uv"
s2 = "abc"
print(s > s2)  # u > a
ls = [1, 2, 3]
ls2 = [2, 3, 1]
print(ls == ls2)  # Fals: compara ordonat
"""

# SORTARE sorted(secventa) => lista
# exista posibilitatea sa specificam si un criteriu de comparare
ls = [4, 1, 2]
print(sorted(ls))
print(ls)  # lista initiala nu se modifica
print(sorted("pauza"))
