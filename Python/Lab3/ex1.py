"""
ex4 matrice
4. Se citesc m, n și o matrice cu m linii și n coloane, elementele unei linii fiind date pe o
linie (elementele unei linii date pe o linie separate cu spațiu). Să se creeze o listă cu
maximele de pe fiecare linie (folosind și comprehensiune)

tip input:
4 3
2 1 4
10 5 7
....
"""
# input().split() => ["4", "3"]
# ls = input().split()
# m, n = int(ls[0]), int(ls[1])
m, n = [int(x) for x in input().split()]
mat = [[int(y) for y in input().split()] for x in range(m)]
maxim = [max(x) for x in mat]
print(maxim)
