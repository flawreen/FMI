"""
Se dă un vector de numere naturale ordonat crescător (toate elementele sale se vor da pe o
linie separate prin spațiu). Sa se elimine duplicatele din vector
"""
ls = [int(x) for x in input().split()]
frecv = [0 for i in range(100)]
for x in ls:
    frecv[x] += 1
for x in ls:
    while frecv[x] > 1:
        ls.remove(x)
        frecv[x] -= 1
print(ls)
