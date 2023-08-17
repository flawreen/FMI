"""
3. Scrieți o funcție cu număr variabil de parametri care să caute un cuvânt dat în mai multe
fișiere text. Funcția va scrie într-un fișier text câte o linie pentru fiecare fișier text de intrare,
astfel: numele fișierului text de intrare și apoi numerele de ordine ale liniilor pe care apare
cuvântul dat în acel fișier (numerotate de la 1) sau un mesaj corespunzător dacă fișierul nu
conține cuvântul respectiv. Antetul funcției va fi: cautare_cuvant(cuv, nume_fis_out,
*nume_fis_in). Se vor număra aparițiile cuvântului fără a face diferența între literă mare și
literă mică. De exemplu, prin apelul cautare_cuvant("floare","rez.txt", "eminescu.txt",
"paunescu.txt") se va căuta cuvântul “floare” în fișierele text “eminescu.txt” și
“paunescu.txt”, iar rezultatul căutării va fi scris în fișierul text “rez.txt”
"""
import re
def cautare(cuv, nume_fis_out, *nume_fis_in):
    g = open(nume_fis_out, "w")
    for fis in nume_fis_in:
        with open(fis, "r") as f:
            i, ok = 1, 0
            g.write(fis[6:])
            for linie in f:
                if cuv.lower() in re.split(r"\W+", linie.lower()):
                    ok = 1
                    g.write(f" {i}")
                i += 1
            if ok == 0:
                g.write(f"{cuv} nu exista")
            g.write("\n")
    g.close()
cautare("floare", "files/cuvant.out", "files/eminescu.txt", "files/paunescu.txt")

