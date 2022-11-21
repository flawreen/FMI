"""
4. În fișierul text “test.in” se află testul unui elev de clasa a II-a la matematică, conținând 9
înmulțiri scrise pe rânduri distincte. Un calcul corect este notat cu un punct, iar unul
incorect cu 0 puncte. Să se realizeze un program care să evalueze testul dat, astfel: în dreptul
fiecărui calcul corect se va scrie mesajul ‘Corect’, iar în dreptul fiecărui calcul greșit se va
scrie mesajul ‘Gresit’ și rezultatul corect, iar la final se va scrie nota (un punct se acordă
din oficiu!). Rezultatul evaluării testului se va afișa în fișierul test.out
Test.out
3*4=11 Gresit 12
2*10=20 Corect
5*5=24 Gresit 25
7*4=28 Corect
2*6=12 Corect
10*10=100 Corect
3*9=27 Corect
6*7=33 Gresit 42
0*9=1 Gresit 0
Nota 6
"""
f = open("files/test.in")
g = open("files/test.out", "w")
puncte = 1
for linie in f:
    linie = linie.rstrip("\n")
    i = linie.index('*')
    x = int(linie[:i])

    j = linie.index('=')
    y = int(linie[i+1:j])

    rez = int(linie[j+1:])

    xy = x * y
    if xy == rez:
        g.write(f"{linie} Corect\n")
        puncte += 1
    else:
        g.write(f"{linie} Gresit {xy}\n")
f.close()
g.write(f"Nota {puncte}")
g.close()
