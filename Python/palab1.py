import math

"""
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

d = b**2 - 4*a*c

if d < 0:
    print("Ecuatia nu are radacini reale.")
elif d == 0:
    x = -b / 2*a
    print(f'Ecuatia are solutiile reale x1 = x2 = {x}')
elif d > 0:
    x1 = -b + math.sqrt(d) / 2 * a
    x2 = -b - math.sqrt(d) / 2 * a
    print(f'Ecuatia are solutiile reale x1 = {x1} si x2 = {x2}')
"""

"""
l1 = int(input("L1 = "))
l2 = int(input("L2 = "))

L = l1 * l2
x, y = l1, l2
x, y = max(x,y), min(x,y)
r = x % y
while r > 0:
    x, y = max(r, y), min(r, y)
    r = x % y

nrPlaci = L // (y**2)
print(f'Mesterul are nevoie de {nrPlaci} placi de gresie, fiecare cu latura de {y}cm.')
"""

"""
x = int(input("x = "))
n = int(input("n = "))
p = int(input("p = "))
m = int(input("m = "))

dist = 0

while m > 0:
    if m > n:
        m -= n
        dist += n * x
        x -= (p/100) * x
    else:
        dist += m * x
        m -= n

print(f'Distanta parcursa de greiere: {dist} cm')
"""

"""
lista = []
n = int(input("n = "))
m = 0
x, y = 0, 0
for i in range(0, n):
    x = float(input())
    lista.append(x)

for i in range(1, n):
    x = lista[i] - lista[i-1]
    if abs(x) > m:
        m = abs(x)
        y = i
print(y+1, y)
"""

"""
n = int(input("n = "))
m1 = int(input())
m2 = int(input())
ok = 0
if abs(m1-m2) > 1e-9:
    ok = 1

for i in range(0, n-2):
    m3 = int(input())
    if ok == 0 and m3 == m1:
        continue
    else:
        ok = 1
        if m3 > m1:
            m1, m2 = m3, m1
        elif m3 > m2:
            m1, m2 = m1, m3

if ok == 0 or m1 == m2:
    print("Imposibil")
else:
    print(m1, m2)
"""



