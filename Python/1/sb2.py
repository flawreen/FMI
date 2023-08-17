A = [3, -2, 5, -1, 4]
B = [7, 8, 2, -5, -4, -1, 5]
rez = []
suma = 0
A.sort(reverse=True)
A.sort(key=lambda x: abs(x), reverse=True)
B.sort(reverse=True)
print(B)
for i in range(len(A)):
	if A[i] < 0:
		suma += A[i] * B[-1]
		rez.append((A[i], B[-1]))
		B.pop()
	else:
		suma += A[i] * B[i]
		rez.append((A[i], B[i]))
print(suma, end=" = ")
print(" + ".join([f"{x[0]} * {x[1]}" for x in rez]))
"""
In acest algoritm am sortat prima lista in ordine descrescatoare cu cheia modul de x, iar cea de-a doua fara cheie, 
apoi am parcurs lista A si am adaugat la suma produsul lui A[i] si B[-1] daca A era negativ, si A[i] * B[i] altfel. 
Astfel, daca A[i] este negativ, va fi inmultit cu cel mai mic numar negativ, obtinand produsul maxim dintre A[i] si 
orice alt element nefolosit din B.

Se incadreaza in metoda Greedy deoarece am sortat lista A descrescator dupa modulul numerelor, astfel incat suma 
iese cu cele mai mari numere din vector.
Criteriul de selectie este corect, deoarece, daca elementele au acelasi semn, se inmultesc, si se adauga la suma 
datorita sortarii descrisa mai sus, iar daca A[i] este negativ, este inmultit cu cel mai mic numar astfel incat 
produsul este mmai mare decat cu orice alt numar din B (nefolosit)
Algoritmul este O(nlogn) din cauza sortarilor, iar for loop-ul este O(n).
"""
# 3 -2 5 -1 4
# 7 8 -5 2 -4 -1 5

