"""
2. a) Scrieți o funcție care primește un număr variabil de parametri și un filtru = o funcție
booleana și returnează o listă cu parametri care verifică filtrul. Dacă la apel nu este transmisă
nicio funcție pentru filtru, atunci se vor returna parametrii primiți.
Exemplu de apel:
def pozitiv(x):
return x>0
a = filtreaza(3,-1,6,8,-3,functie=pozitiv)
print(a)
a = filtreaza(3,-1,6,8,-3)
print(a)
a = filtreaza("ana","are","10","mere",functie=str.isalpha)
print(a)
"""
def pozitiv(x):
    return x>0
def filtreaza(*args, functie=None):
    if functie == None:
        return list(args)
    return [x for x in args if functie(x)]

a = filtreaza(3, -1, 6, 8, -3, functie=pozitiv)
print(a)
a = filtreaza(3, -1, 6, 8, -3)
print(a)
a = filtreaza("ana","are","10","mere",functie=str.isalpha)
print(a)
"""
b) Modificați antetul de la a astfel încât funcția să primească parametru o listă pe care să o
filtreze (nu un număr variabil de parametri). Exemplu de apel:
a = filtreaza([3,-1,6,8,-3],functie=pozitiv)
print(a)
"""
def filtreaza(ls, functie=int):
    n = len(ls) - 1
    while n > 0:
        if not functie(ls[n]):
            ls.pop(n)
            n -= 1
        else:
            n -= 1
    return ls
a = filtreaza([3,-1,6,8,-3],functie=pozitiv)
print(a)
