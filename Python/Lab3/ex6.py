"""
Se dă o listă de numere naturale și un număr natural k. Să se elimine din listă subsecveța
de lungime k de sumă minimă (dacă sunt mai multe se va elimine prima = cea mai din
stânga) – fără a folosi liste suplimentare
"""
ls = [int(x) for x in input().split()]
k = int(input())
"""
# Metoda 1 - complexitate mai mare
n = len(ls)
min = sum(ls[:k])
j = (0, k)
for i in range(1, n):
    if sum(ls[i:i+k]) < min:
        min = sum(ls[i:i+k])
        j = (i, i+k)
del ls[j[0]:j[1]]"""

# Metoda 2
i = 0
n = len(ls)
min = sum(ls[:k])
rez = [0, k-1]
i += 1
while k < n:
    if ls[k] < ls[i-1]:
        min = min - ls[i-1] + ls[k]
        rez[0], rez[1] = i, k
    k += 1
    i += 1

del ls[rez[0]:rez[1]+1]
print(ls)