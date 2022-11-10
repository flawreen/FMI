"""
Se citesc m, n și o matrice cu m linii și n coloane, elementele unei linii fiind date pe o
linie (elementele unei linii date pe o linie separate cu spațiu). Să se determine numărul de
valori pare din matrice (folosind și comprehensiune)
https://www.pbinfo.ro/probleme/767/sumapare2
"""
m, n = [int(x) for x in input().split()]
mat = [[int(x) for x in input().split()] for _ in range(m)]
nrPare = [x for linie in mat for x in linie if x % 2 == 0]
nrPare = len(nrPare)
print(nrPare)

