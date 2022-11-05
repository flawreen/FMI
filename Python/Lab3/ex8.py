"""
Se dă o listă de numere reale (toate elementele sale se vor da pe o linie separate prin spațiu).
Să se insereze câte un 0 după fiecare element negativ (fără a folosi liste suplimentare)
"""
ls = [float(x) for x in input().split()]
n = len(ls)
i = 0
while i < n:
    if ls[i] < 0.0:
        ls[i+1:i+1] = [0.0]
        n += 1
    i += 1
print(ls)
