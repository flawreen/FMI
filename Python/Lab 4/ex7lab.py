"""
7. În fișierul "elevi.in" sunt memorate informații despre elevii unei clase; astfel, pe o linie a
fișierului se dau următoarele informații despre un elev: cnp, nume (fără spații), prenume
(fără spații), lista de note, de exemplu:
2501910000034 Ionescu Ion 10 8 7 8
2402900000041 Marinica Maria 9 10 8 8 8
1412900000041 Petrescu Petrica 8 10 4 7

a) Memorați lista de elevi din fișier astfel încât să se poată răspundă cât mai eficient la
întrebări de tipul celor de la subpunctele următoare (dat cnp elev, care sunt numele, notele,
să se lista de note a elevului).
"""
from string import ascii_letters, digits
from random import choices
f = open("files/elevi.in", "r")
d = {}
for linie in f:
    linie = linie.split()
    cnp, nume, prenume = linie[0], linie[1], linie[2]
    note = [int(linie[x]) for x in range(3, len(linie))]
    d[cnp] = [nume, prenume, note]
f.close()
"""
b) Scrieți o funcție care primește ca parametri un cnp și structura de date în care s-au
memorat datele despre elevi la punctul a) și crește cu 1 prima notă a elevului cu cnp-ul
primit ca parametru. Funcția returnează nota după modificare sau None dacă cnp-ul nu
există. Apelați funcția pentru un cnp citit de la tastatură.
"""
def cresteNota(cnp, date):
    if cnp in date:
        date[cnp][2][0] += 1
        return date[cnp][2][0]
    else:
        return None
# c = input()
# print(cresteNota(c, d))
"""
c) Scrieți o funcție care primește ca parametri un cnp, o listă de note și structura de date în
care s-au memorat datele despre elevi la punctul a) și adaugă lista de note la notele elevului
cu cnp-ul primit ca parametru. Funcția returnează lista de note după modificare sau None
dacă cnp-ul nu există. Apelați funcția pentru un cnp citit de la tastatură si lista
l_note=[10,8].
"""
def adaugaNote(cnp, l_note, date):
    if cnp in date:
        date[cnp][2].extend(l_note)
        return date[cnp][2]
    else:
        return None
# l_note = [10, 8]
# print(adaugaNote('1412900000041', l_note, d))
"""
d) Scrieți o funcție care primește ca parametri un cnp și structura de date în care s-au
memorat datele despre elevi la punctul a) și șterge informațiile despre elevul cu acest cnp.
Apelați funcția pentru un cnp citit de la tastatură (dacă cnp-ul nu este în listă funcția nu va
modifica nimic și nu va da eroare)
"""
def stergeElev(cnp, date):
    date.pop(cnp)
# stergeElev('1412900000041', d)
"""
e) Folosind structura de date în care s-au memorat datele despre elevi la punctul a) (nu
citind din nou datele) construiți în memorie o lista de liste cu elevii din fișier, un element
din lista fiind de forma [nume, prenume, lista de note], ordonată descrescător după medie
și, în caz de egalitate, după nume și afișați elementele listei în fișierul „elevi.out”.
"""
def sortMedie(x):
    medie = sum(x[2]) / len(x[2])
    return medie, x[0]

ls_elevi = list(d.values())
ls_elevi.sort(key=sortMedie, reverse=True)

g = open("files/elevi.out", "w")
for elev in ls_elevi:
    g.write(f"{elev[0]} ")
    g.write(f"{elev[1]} ")
    g.write(" ".join(f"{x}" for x in elev[2]))
    g.write("\n")
g.close()
"""
f) Scrieți o funcție care primește ca parametru structura de date în care s-au memorat datele
despre elevi la punctul a) și adaugă la informațiile asociate unui student un cod de lungime
6 generat aleator care conține 3 litere urmate de 3 cifre. 

Exemplu de apel:
genereaza_coduri(d)
print(d)
"""
def genereaza_coduri(date):
    for ch in date:
        cod = "".join(choices(ascii_letters, k=3)) + "".join(choices(digits, k=3))
        d[ch].append(cod)
genereaza_coduri(d)
print(d)

