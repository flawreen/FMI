"""
Se citesc m, n și o matrice cu m linii și n coloane, elementele unei linii fiind date pe o
linie (elementele unei linii date pe o linie separate cu spațiu). Să se determine să
determine, pentru fiecare linie, cea mai mică valoare care se poate obține adunând
elementele de pe linie, cu excepția unuia. (folosind și comprehensiune).
https://www.pbinfo.ro/probleme/659/sumalinii1
"""
m, n = [int(x) for x in input().split()]
mat = [[int(x) for x in input().split()] for _ in range(m)]
minim = [sum([x for x in linie if x != max(linie)]) for linie in mat]
print(minim)
