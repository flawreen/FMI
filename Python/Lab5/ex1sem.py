"""
1. Se citește un vector de numere naturale (cu elementele date pe o linie, separate prin
spațiu). Să de ordoneze elementele din vector crescător după suma cifrelor, iar în caz de
egalitate, descrescător după valorile lor
v = [11, 45, 20, 810, 179, 81, 1000] => v = [1000, 20, 11, 810, 81, 45, 179]
"""
def cifre(x):
    s = 0
    xx = x
    while x > 0:
        s += x%10
        x//=10
    return s, -xx

ls = [11, 45, 20, 810, 179, 81, 1000]
ls.sort(key=cifre)
print(ls)


