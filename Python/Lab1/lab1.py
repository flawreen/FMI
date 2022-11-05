#lab1 ex 7

"""
n = int(input("n="))

# pe o singura linie separata cu spatiu
s = input()  # iese str
rez = 0
lista_nr = s.split()  # tot str
for x in lista_nr:
    x = int(x)
    rez = rez ^ x  # daca facem XOR cu toate ramane doar cel care nu apare de doua ori

print(rez)
"""

# ex 8
"""
s = input()
lista_nr = s.split()
k = 0
n = len(lista_nr) + 1
for i in lista_nr:
    x = int(i)
    k = k ^ x

k1 = k ^ n - n + 1  # var 1
print(f'Varianta 1: {k1}')

for i in range(1, n+1):
    k = k ^ i

print(f'Varianta 2: {k}')
"""

#ex 9
"""
n = int(input("n="))
k = int(input("k="))
b = int(input("b="))
print(bin(n))
# var 1
# n = (n >> (k-1) | b) << (k-1) | n
# var 2
# n = n | (1 << k-1)???

print(bin(n))
"""

#ex 5 Fibonacci
a = int(input("a="))
b = int(input("b="))
x = y = 1
while x < a:
    x, y = y, x + y
print(x)











