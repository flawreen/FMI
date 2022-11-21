"""
6. Se consideră un fișier de intrare produse.in cu informații despre magazine, produse și
cantitatea de produse din fiecare magazin, sub forma:

Magazin cod_magazin nume_magazin
cantitate nume_produs
...
cantitate nume_produs
Magazin cod_magazin nume_magazin
cantitate nume_produs
...
cantitate nume_produs

Exemplu:

Magazin 123 magazin1
5 mere
7 pere
2 prune
Magazin 221 magazin 2
3.5 pere
10 banane

a) Să se memoreze datele astfel încât să răspundă la interogări de tipul: dat codul
magazinului și numele unui produs, să se afișeze cantitatea de produs din magazin (să se
interogheze pentru un cod și un nume date de la tastatură).
Dat codul magazinului, numele unui produs și o cantitate de produs care se vinde, actualizează
stocul de produs dinmagazin dacă se poate (să se facă o astfel de actualizare pentru cod, nume produs, cantitate
date de la tastatură)
"""
f = open("files/produse.in", "r")
mag = {}
for linie in f:
    linie = linie.split()
    if linie[0] == "Magazin":
        mag[linie[1]] = (" ".join(linie[2:]),{})
        # mag[linie[1]][0] = " ".join(linie[2:])
        # mag[linie[1]].append({})
        x = linie[1]
    else:
        mag[x][1][linie[1]] = float(linie[0])

def interogare(cod, produs):
    if cod in mag:
        prod = mag[cod][1].get(produs, "Produsul nu exista!")
        if isinstance(prod, str):
            print(prod)
        return prod
    else:
        print("Magazinul nu exista!")

def vinde(cod, produs, cant):
    if isinstance(interogare(cod, produs), float):
        if cant <= mag[cod][1][produs]:
            mag[cod][1][produs] -= cant
            print(f"Stoc actualizat: {mag[cod][1][produs]}")
        else:
            print("Stoc insuficient!")

# cod, produs, cant = input(), input(), float(input())
# vinde(cod, produs, cant)
"""
b) Să se afișeze o lista de tupluri (nume_magazin, stoc_marfa) ordonată după cantitatea
totală de marfă din magazin, și, în caz de egalitate, după numele magazinului
"""
produse = list(mag.values())
produse.sort(key=lambda x: x[0])
produse.sort(key=lambda x: sum(list(x[1].values())), reverse=True)
print(produse)
"""
c) Să se afișeze o listă a tuturor produselor care se găsesc în magazine (folosind reuniune
de mulțimi)
"""
ls_prod = set()
for ch in mag:
    ls_prod |= set(mag[ch][1])
print(list(ls_prod))
