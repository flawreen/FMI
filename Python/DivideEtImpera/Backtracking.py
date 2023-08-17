"""
Metoda Backtracking

Cadru -> set vectori x = (x1, x2, ..., xn) care verifica o anumita propr (cond finala)
						  X1  X2       Xn  <- valori posibile pt fiecare element din vector

Exp -> generarea permutarilor multimii {1, 2, ..., n}
	sol: x = (x1, x2, ..., xn) xi apartine {1, ..., n}
	Cond finala: xi != xj, oricare i != j (distincte)
	(1, 2, 2, 2)

n = 3
1 1 -> nu continuam completarea solutiei
		putem obtine o permutare
1 2 -> putem continua -> trecem la poz urmatoare
1 2 1 -> nu
1 2 2 -> nu
1 2 3 -> da
"""
