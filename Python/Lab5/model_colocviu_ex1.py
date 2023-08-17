"""
a) [0.5 p.] Scrieți o funcție citire_numere cu un parametru reprezentând numele unui fișier text
care conține, pe mai multe linii, numere naturale despărțite între ele prin spații și returnează o
listă de liste (numite subliste), elementele unei subliste fiind numerele de pe o linie din fișier.
"""
def citire_numere(nume_fisier):
    f = open(nume_fisier)
    mat = [[int(x) for x in linie.split()] for linie in f]
    # with open(nume_fisier, "r") as f:
    #     for linie in f:
    #         ls = [int(x) for x in linie.split()]
    #         mat.append(ls)
    return mat
"""
b) [2 p.] Să se scrie o funcție prelucrare_lista care primește ca parametru o listă de liste pe care
o modifică astfel:
• din fiecare sublistă se vor elimina toate aparițiile valorii minime, apoi
• din fiecare sublistă se vor păstra doar primele m elemente, unde m reprezintă lungimea
minimă a unei subliste.
"""
def prelucrare_lista(matrix):
    min_len = len(matrix[0])
    for linie in matrix:
        min_val = min(linie)
        leng = len(linie)
        for i in range(leng-1, -1, -1):
            if linie[i] == min_val:
                del linie[i]
                leng -= 1
        if leng < min_len:
            min_len = leng

    for linie in matrix:
        linie[:] = linie[:min_len]
        # Sau del linie[min_len:]
"""
c) [0.5 p.] Se dă fișierul "numere.in" cu următoarea structură: pe linia 𝑖 se află separate prin câte
un spațiu 𝑛 numere naturale reprezentând elementele de pe linia 𝑖 a unei matrice, ca în exemplul
de mai jos. Să se apeleze funcția prelucrare_lista pentru matricea obținută în urma apelului
funcției citire_numere pentru fișierul text numere.in. Matricea astfel obținută să se afișeze pe
ecran, fără paranteze și virgule, iar elementele de pe fiecare linie să fie separate prin câte un
spațiu.
"""
def afisare_lista(matrix):
    print("\n".join([" ".join([f"{x:4}" for x in linie]) for linie in matrix]))
"""
d) [1 p.] Fie L matricea (memorată ca listă de liste) obținută în urma apelării funcției citire_numere
pentru fișierul text "numere.in". Să se citească de la tastatură un număr natural nenul k și apoi
să se scrie în fișierul text "cifre.out" elementele matricei L care sunt formate din exact k cifre sau
mesajul “Imposibil!” dacă nu există niciun element cu proprietatea cerută. Elementele vor fi
scrise în fișier în ordine descrescătoare și fără duplicate.
"""
k = int(input())
mat = citire_numere("files/numere.in")
lim_inf = 10**(k-1)
lim_sup = 10**(k)
knum = {x for linie in mat for x in linie if lim_inf <= x < lim_sup}
# knum = {x: 1 for linie in mat for x in linie if lim_inf <= x < lim_sup}
if len(knum) > 0:
    # knum = list(knum.keys())
    # knum.sort(reverse=True)
    with open("files/cifre.out", "w") as f:
        # f.write(" ".join(str(x) for x in knum))
        knum = sorted(knum, reverse=True)
        f.write(" ".join(str(x) for x in knum))
else:
    print("Imposibil!")



