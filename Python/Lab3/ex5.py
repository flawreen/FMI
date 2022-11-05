"""
Se dă o listă de numere naturale. Să se șteargă din listă toate zerourile
"""
ls = [int(x) for x in input().split()]
# Varianta 1
try:
    poz = ls.index(0)
except ValueError:
    print("Lista nu are niciun 0.")

try:
    while(True):
        ls.pop(poz)  # sau del ls[poz]
        poz = ls.index(0, poz)
except ValueError:
    pass
#Varianta 2
# ls[:] = [x for x in ls if x != 0]  # face alta lista dar e O(n)
print(ls)
