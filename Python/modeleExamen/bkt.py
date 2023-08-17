"""
S = (x1, x2, ..., xk-1, xk, xk+1, ..., xn)
xk = componenta curenta
x1, ..., xk-1 -> secv OK -> s.n. sol partiala

Backtracking incearca sa extinda o solutie partiala catre o solutie completa

exp:
n = 5
S = (1, 5, 2, 1 (nu e bun), 1(nu e bun))
			  2 (nu e bun), 2(nu e bun)
			  3 (e bun),    3 (nu e bun)
			  				4(nu e bun)
			  				5 (nu e bun) -> ma intorc la componenta anterioara
			  4(e bun)      4(nu e bun)
			  				5(nu e bun) -> ma intorc la componenta anterioara
			  5(nu e bun) -> ma intorc la componenta anterioara

In Backtracking miscarea orizontala este bidirectionala:
inainte cand (x1, ..., xk-1) este solutie partiala
inapoi cand am testat toate val. pos. pt xk

pt xk avem o miscare verticala bidirectionala
	-> mink = cea mai mica valoare posibila  |
	-> maxk = cea mai mare valoare posibila  |
											 v
								nu verifica conditiile de continuare

+ Forma generala:

def bkt(k):  # k=indicele componentei curente(xk)
	uneori va fi nevoie de global n, x
	for v in range(mink, maxk+1):  # (1)  trecerea pe verticala    v este variabila locala, forul stie mereu unde a
		# ramas
		x[k] = v
		if x[1], ..., x[k] este sol partiala:  # (2)
			if x[1], ..., x[k] este sol:  # (3)  trecerea orizontala pe DREAPTA
				print(x)
			else:
				bkt(k+1)

+ Generarea permutarilor de lungime n:
Permutarile sunt aranjamente de n luate cate n
(1) mink = 1, maxk = n
(2) x[k] not in x[1:k]
(3) k == n
..............
n = int(input("n="))
x = [0 for _ in range(n+1)]
bkt(1)


Daca intr-un fisier ai pe cate o linie toate permutarile de lungime n
care e  complexitatea sa afisezi continutul fisierului pe ecran? n * n!
n! linii
n sa afisezi o linie

+ Generarea aranjamentelor:
A ->n elem
Aranj de m elemente (din cele n) = tupluri (conteaza ordinea elementelor) cu m elemente
												(1, 2, 3) != (1, 3, 2)
A de m luate cate n = n! / (n-m)!
A 5 cate 3 = 5! / 2! = 60

(1) mink = 1, maxk = n
(2) x[k] not in x[1:k]
(3) k == n
Complexitate: O(A de m luate cate n)


+ Generarea combinarilor:
Combinari de m elemente ale unei multimi cu n elemente = submultimi cu m elemente
															NU conteaza ordinea elementelor
Ca sa ne asiguram ca xk este mereu termen corect, xk < xk-1 pt oricare k
C m cate n = A m cate n / m!
(1) mink = mink-1 + 1, maxk = n
min0 = 0
(2) ----- se elimina complet if-ul de la solutie partiala
(3) k == m
Complexitate O(C m cate n)


probleme mai serioase:

+ Descompunerea unui nr natural ca suma de numere naturale nenule (problema de partitie)
x[k] = un termen al sumei
(1) mink = 1, maxk = n
(2) sum(x[1:k+1]) <= n
(3) sum(x[1:k+1]) == n

+ Plata unei sume folosind n tipuri de monede
S = 12e
v = (2, 3, 5)e
x = (2, 1, 1)
x[k] = nr monedelor cu val v[k]
(1) mink = 0, maxk = S // v[k]
(2) sum([x[k] * v[k] for k in range(1, n+1)]) <= S
(3) sum de ce e la 2 == S
.....
else:
	if k < n:
		bkt(k+1)
"""














