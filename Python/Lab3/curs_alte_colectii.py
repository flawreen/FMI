"""
# vector de cifre => SSD frecv fiecarei cifre in vector
v = [int(x) for x in input().split()]
frecv = [0 for i in range(10)]
for x in v:
    frecv[x] += 1
print(frecv)
"""
"""
propozitie -> frecventa fiecarui cuvant in propozitie
prop = "mere pere mere are pere prune mere"

tabele indate dupa alte tipuri de chei decat numere mici
dictionare - tabele dispersie
"""
prop = "mere pere mere are pere prune mere"
d = {}
for cuv in prop.split():
    if cuv in d:  # => O(1)? cautare/accesare eficienta a cheii
        d[cuv] += 1  # d[cuv] => O(1)
    else:
        d[cuv] = 1
print(d)
"""
+++ Tabele de dispersie
= structuri de date indexate dupa chei care au asociate un cod numeric, numit code hash
(functie de dispersie), a carui valoare nu se schimba e parcrsul existentei cheii 
(de aceea cheia trebuie sa fie imutabil)
Doua obiecte cu valori egale au acelasi code hash
Ideal ar fi ca doua obiecte cu valri diferite sa aiba 
coduri hash diferite, dar acest lucru de obicei nu e posibil pentru ca plaja de valori pe care o pot lua obiectele este mai mare
apar coliziuni (obiecte diferite cu acelasi cod hash)
tabelele de dispersie sunt implementate cat sa optimizee cautarea dupa cheie
in principiu, cautarea in tabel se face astfel:
cheie => se transforma in index numeric hash(cheie) %  wrap
lungimea tabelului => in t[index] se cauta cheia (!!!!! 
y[index] contine informatii despre toate cheile pentru 
care hash(cheie) % lungimea tabelului are aceeasi valoare (
pentru coliziuni)
=> putem folosi ca si cheie doar obieccte care au hash (in general imutabile)
"""

"""
+++ Alte tipuri de colectii  - multimi si dictionare
nu mai sunt indexate dupa indici numerici, de la 0 => nu s[i]

# MULTIMI - tipul set
= colectie de obiecte cu valori diferite
elementele care se pot adaiga in set - imutabile
#CREARE - cu {}, ca si dictionarul
s = {3, 1, 2}
print(s, type(s))
s = set(iterabil)

"""
s = {3, 1, 2}
print(s, type(s))
# ordinea de parcurgere a elementelor - nu este neaparat cea de la creare/inserare
# det literele distincte dintr-un cuvant
s = set("avem un cuvant")
print(s)
# elementele distincte dintr-o lista
ls = [2, 1, 4, 2, 1, 1, 1]
print(set(ls))

# !!!!! multimea vida
s = {}  # dictionar, nu multimea vida
s = set()
# comprehensiune - DA
print("elementele distincte pozitive")
ls = [2, 1, 4, -2, 1, -1, -1]
s = {x for x in ls if x > 0}
print(s)