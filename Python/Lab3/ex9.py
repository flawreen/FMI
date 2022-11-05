"""
Se citesc doi vectori (elementele fiecăruia fiind date pe o linie separate prin spațiu) de
numere naturale de exact două cifre (elementele vectorilor nu sunt neapărat distincte). Să
se determine dacă cei doi vectori sunt egali (folosind vector de frecvențe vs folosind sorted)
"""
l1 = [int(x) for x in input().split()]
l2 = [int(x) for x in input().split()]
frecv = [0 for i in range(100)]
for x in l1:
    frecv[x] += 1
for x in l2:
    frecv[x] -= 1
if min(frecv) == max(frecv) == 0:
    print("Vectorii au toate elementele egale.")
else:
    print("Vectorii nu au toate elementele egale.")

