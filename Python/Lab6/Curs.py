"""
Programare dinamica

- det unor subp utile pentru rezolvarea pb -> care se suprapun
- det unor relatii de recurenta pt rezolvarea subob (de obicei deduc dintr-un principiu de optimalitate)
memorizare -> se memoreaza rezultatele subpb deja calc (pt a nu rezolva o subpb de mai multe ori)

Etape:
1) Det care sunt subpb utile
2) Cum obtinem rez pb initiale din subp
3) Rel de recurenta - pt subpb
4) Ordinea de calcul pt rel de recurenta (+ce stim sa rezolvam direct)

Pb1: pb de trasee optime
Se da o matrice triunghiulara de dim n de nr naturale. Sa se det un traseu de suma maxima in matrice care respecta urmatoarele reguli de deplasare:
    - pornim de pe prima linie (1, 1)
    - din celula (i, j) ne putem deplasa pe linia urmatoare in celulele (i+1, j) sau (i+1, j+1)
    - trebuie sa ajungem pe ultima linie
    3
    9  10
t = 5  2  1
    4  7  1  4
    10 11 2  3  1
           __ (i+1, j)
(i, j) -->|
           -- (i+1, j+1)
avem de ales intre 2 variante. Daca am sti care este suma max pe care vom obtine pornind din (i+1, j), respectiv (i+1, j+1) am sti in care dintre doua celule sa ne deplasam
Subpb: s[i][j] = suma max pe care o putem obtine incepand din celula (i, j)
Solutia va fi s[1][1]
Relatia de recurenta: s[i][j] = t[i][j] + max{s[i+1][j], s[i+1][j+1]} ce e in max e deja calculat
Ordinea de calcul pt s -> de la ultima linie catre prima
    Stim direct sa calc ultima linie s[n][i] = t[n][i]
    35
    32 30
s = 23 20 8
    15 18 4 7
    10 11 2 3 1
15 = s[n-1][1] = t[n-1][1] + max{s[n][1], s[n][2]}
                    =4          =10         =11
Solutia s[1][1]
Constr unui traseu - pornind din (1, 1) si mergand mereu in s in vecinul cu s maxim (dintre s[i+1][j] si s[i+1][j+1])


Var 2 subpb: s[i][j] = suma maxima a unui traseu care se termina cu (i, j) (si porneste din (1, 1))
 sol pb -> max de pe ultima linie
"""
from copy import deepcopy
f = open("files/triunghi.txt")
ls = [[int(x) for x in ln.split()] for ln in f]
lt = deepcopy(ls)
""" 
in lt e rezultatul
in for fac lt[i][j] = ls[i][j] + lt[i+1][j] (sau lt[i+1][j+1])
"""
leng = len(ls)-2
for i in range(leng, -1, -1):
	for j in range(i+1):
		lt[i][j] += max(lt[i+1][j], lt[i+1][j+1])
print(lt[0][0])
