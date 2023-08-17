"""
1. O funcție care calculează suma f(i) cu i=1,n.
Cu ajutorul ei putem calcula, de exemplu, suma
primelor n numere naturale, a primelor n pătrate perfecte etc
"""
import math
def inv(i):
    return 1/i

def suma(*arg, functie = int):
    s = 0
    for x in arg:
        s += functie(x)
    return s

# print(suma(1,2,3,4))
# print(suma(1,2,3,4, functie=lambda x: x*x))
# print(suma(1,2,3,4, functie=math.sqrt))
"""
2. Filtrarea unei liste după un criteriu (dat printr-o funcție care returnează True/False)
"""
def pozitiv(x):
    return x > 0
def filtreaza(ls, fc):
    return [x for x in ls if fc(x)]
l = filtreaza([3, -1, 6, 8, -3], pozitiv)
# print(l)
def filtreaza(*ls, fc):
    return (x for x in ls if fc(x))
l = filtreaza(3, -1, 6, 8, -3, fc=pozitiv)
# print(l)
# print("filtr", 1)
"""
Exercițiu: Scrieți o funcție care primește ca parametru un număr variabil de numere x1,...,xn și o funcție f și calculează media:
suma de f(xi) / n cu i=1,n
"""
def scad(x):
    return x-1
def media(*args, functie = int):
    s = 0
    for x in args:
        s += functie(x)
    return s / len(args)

print(media(2, 3, 4, 5, 6, functie=scad))

