"""
Se dă o listă de numere naturale. Să se șteargă din listă subsecvența delimitată de primele
două zerouri din listă (inclusiv zerourile)
"""
ls = [int(x) for x in input().split()]
i = ls.index(0)
try:
    j = ls.index(0, i+1)
    ls[i:j + 1] = []
    print(ls)
except ValueError:
    print("Lista nu are mai multe 0-uri.")

