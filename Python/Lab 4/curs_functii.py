"""
functia se apeleaza cu parametri actuali/efectivi
(valori sau expresii care se transmit la apelul functiei)
"""
def f(x):  # parametru formal x
    print(x)
f(3+5)  # parametru actual 3+5

"""
+++ Returneaza - orice tip de date si oricate valori (separate cu virgula => tuplu)
daca nu returneaza ceva explicit - returneaza None
"""
print("Returneaza")
print(f(3+5))
ls = [5, 3]
print(sorted(ls))
print(ls.sort())  # None

"""
+++ Transmiterea parametrilor
parametrii se trimit prin atribuire (se transmite prin valoare referinta catre obiect)
=> singurele modificari vizibile in afara dupa incheierea executiei functiei sunt cele facute asupra valorilor parametrilor mutabili
"""
print("Transmiterea parametrilor")
def modifica(x):
    x = 8
    print(x)  # -> 8
a = 9
modifica(a)
print(a)  # -> 9

def creare(ls):
    ls = [1, 2, 3]  # nou obiect => se modifica referinta
ls = []
creare(ls)
print(ls)  # -> []

def creare(ls):
    ls.extend([1, 2, 3])  # nu cream nou obiect => modific valoarea celui existent
ls = []
creare(ls)
print(ls)  # -> [1, 2, 3]

""""
+++ Domeniul de vizibilitate
la interogare - variabila este cautata in spatiul curent, apoi in cel global; 
mai exact - regula LEGB(Local, Enclosing(pt functii incluse in alte functii), Global, B-build)
"""
print("Domeniul de vizibilitate")
def f():
    print(x)
x = 80
f()
"""
o variabila se creeaza prima data cand i se atribuie o valoare
la prima atribuire intalnite, daca variabila nu exista in spatiul curent, se creeaza 
(!!!!!!!!!! la atribuire nu o cauta LEGB)
"""
def f():
    x = 15  # Cauta x in local, nu exista, il creeaza
    print(x)  # -> 15

def g():
    print(x)  # -> UnboundLocalError: local variable 'x' referenced before assignment
    x = 15

def h():
    global x  # specificam spatiul(domeniul) unde cauta variabila
    print(x)
    x = 15
x = 90
f()
# g()
h()
print(x)  # -> 90

"""
+++ Tipuri de parametri
- parametri obligatorii (trebuie sa primeasca obligatoriu la apel) - folositi pana acum
- parametri cu valoare implicita, atribuita in antet (optionali - pot lipsi la apel => se foloseste val implicita)
- parametri cu numar variabil de parametri (parametru care aduna in el mai multe valori)

+++ Parametri obligatorii
la apelul functiei putem trimite valori pt parametri obligatorii:
- prin pozitie (param actuali respecta ordinea si numarul param din antet)
- prin nume: nume_param = valoare => nu mai trebuie respectata ordinea
se pot combina - dar intai se dau cei prin pozitie

in anumite contexte este obligatoriu ca param sa fie dati prin pozitie (positional only)
sau obligatoriu prin nume (keyword only argument)
"""
print("Tipuri de parametri")
def scrie(x, y, z):  # prin pozitie
    print(x, y, z)
scrie(1, 2, 3)
scrie(y=2, x=1, z=3)  # prin nume
scrie(1, z=3, y=2)
"""
SUPLIMENTAR
putem specifica in antet ca este obligatoriu ca param sa fie dati prin pozitie
scrie(x, y, z, /)
sau obligatoriu din nume
scrie(*, x, y, z)
"""

"""
Parametri cu valori default (implicite) - in antet dupa cei obligatorii
exp: index(x), index(x, start)...
"""
def suma(lista, lim_inf=0, lim_sup=100):  # suma elementelor din lista intre limite
    s = 0
    for x in lista:
        if lim_inf <= x <= lim_sup:
            s += x
    return s

lista=[-1, 3, 6, 120, 2]
print(suma(lista))  # elementele din [0, 100] - val implicite pt lim
print(suma(lista, 5))  # lim_inf devine 5, la lim_sup ramane val default
print(suma(lista, 5, 150))
print(suma(lista, lim_sup=150))
