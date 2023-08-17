ls = [int(x) for x in input().split()]  # (O(n)) cu n = len(ls)
r = int(input())
suma = 0
ls.sort(key=lambda x: abs(x), reverse=True)  # O(nlogn)
for i in range(len(ls)):
	if r > 0 > ls[i]:
		ls[i] *= -1
		r -= 1
	suma += ls[i]
print(suma, ls, sep="\n")
"""
In acest algoritm am sortat cartonasele descrescator dupa valoarea lor din modul. Astfel, am putut sa parcurg 
vectorul o singura data in O(n) si sa inversez primele r cartonase negative, obtinand suma maxima astfel.
Se incadreaza in tehnica Greedy datorita sortarii pe care am facut-o, cele mai mari cartonase sunt primele in lista 
indiferent de semn, astfel pot inversa valorile negative, dar care inversate au cea mai mare valoare, si valorile 
negative mici sunt ultimele in lista, influentand cel mai putin suma.
Criterul de selectie:
Am selectat elementele in ordinea in care apareau in lista dupa sortare, si am inversat primele r elemente negative cu cea 
mai mare valoare, astfel, suma a fost maxima.
Daca nu as fi sortat dupa modulul numerelor, as fi inversat primele r cele mai apropiate de 0 si suma ar fi fost mai 
mica, pentru ca suma scade mai mult cu elementele mai departate de 0.
"""

