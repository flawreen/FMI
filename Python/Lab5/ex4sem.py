"""
4. a) Scrieți o funcție generică de căutare având următorul antet: cautare(x, L, cmpValori)
Funcția trebuie să returneze indexul ultimei apariții a valorii x în lista L sau None dacă valoarea
x nu se găsește în listă. Funcția comparator cmpValori se consideră că primește 2 parametri și
returnează True dacă valorile primite ca parametrii sunt egale sau False în caz contrar.
"""
def cmpValori(x, y):
    return x==y
def cautare(x, L, cmpValori):
    for i in range(len(L)-1, -1, -1):
        if cmpValori(x, L[i]):
            return i
    return None
print(cautare(3, [3,-1,6,8,-3], cmpValori))
"""
b) Se consideră lista de perechi (tupluri) l_pairs ale cărei elemente se citesc din fișierul
perechi.txt (numerele dintr-o pereche sunt date pe o linie, separate prin -). Se citesc două
numere x și y de la tastatură. Folosind un singur apel al funcției de la a) să se verifice dacă lista
conține perechea (x,y) sau perechea (y,x) și, în caz afirmativ, afișează indexul ultimei apariții
ale unei astfel de perechi.
"""
a, b = 5, 6
f = open("files/perechi.txt")
l_pairs = []
for linie in f:
    ls = linie.rstrip('\n').split("-")
    l_pairs.append((int(ls[0]), int(ls[1])))
f.close()
def compTuplu(x, y):
    if x == y or x == y[::-1]:
        return True
    return False
print(cautare((a, b), l_pairs, compTuplu))
""" 
c) (Temă) Scrieți o funcție care să afișeze, folosind apeluri utile ale funcției cautare, mesajul
DA în cazul în care o listă L formată din n numere întregi este modulo-palindrom sau mesajul
NU în caz contrar. O listă este modulo-palindrom dacă prin parcurgerea modulelor elementelor
sale de la dreapta la stânga sau de la stânga la dreapta se obține aceeași listă.
De exemplu, lista L=[101,17,-101,13,5,-13,101,17,-101] este palindrom.
"""
L = [101,17,-101,13,5,-13,101,17,-101]
def palindrom(ls):
    l = len(ls)
    for i in range(l//2+1):
        c = l-1-i
        if cautare(ls[i], L, cmpValori) != c and cautare(-ls[i], L, cmpValori) != c:
            print("NU")
            return
    print("DA")
palindrom(L)



