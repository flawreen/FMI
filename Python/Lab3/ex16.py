"""
11. Se dă un număr natural n>2. Să se afișeze primele n linii din triunghiul lui Pascal (daca c
este numărul maxim de cifre ale unui număr din triunghi, toate numerele se vor afișa pe
c+1 caractere). De exemplu, pentru n=6 se va afișa
0: 1
1: 1 1
2: 1 2 1
3: 1 3 3 1
4: 1 4 6 4 1
5: 1 5 10 10 5 1
"""
from copy import deepcopy
n = int(input())
print(f"1\n1 1")
v = [1, 1]
for i in range(3, n+1):
    print("1", end=" ")
    x = [1]
    for j in range(1, i-1):
        z = v[j] + v[j-1]
        x.append(z)
        print(f"{z}", end=" ")
    print("1", end="\n")
    x.append(1)
    v = deepcopy(x)
