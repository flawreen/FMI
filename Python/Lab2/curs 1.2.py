# Siruri de caractere - Clasa str
# CREARE:
s = "un sir"
s = 'un sir'  # nu exista char
s = """un sir
pe mai multe linii"""
s = '''un sir
pe mai multe linii'''

# constructor str - pentru conversie
s = str(13.5)
print(s)
s = str(1 == 2)
print(s)
s = str()
print(s)
# caractere speciale, secv escape \n, \t, \'
s = 'it\'s time \u0103'  # sau "it's time"
print(s)
# este imutabil, nu putem modifica valoarea unui caracter din sir
# s[0] = "a" -> NU


# Cautare
# find(element, start, end) - similara cu index, dar returneaza -1, dc nu gaseste
# rfind, rindex - pozitia primei aparitii de la dreapta la stanga (invers)
# Exercitiu - toate poz pe care apare un caracter folosind find
s = "acesta este un sir"
c = "a"
poz = s.find(c)
while poz != -1:
    print(poz, end=" ")
    poz = s.find(c, poz + 1)
print()
# Modificarea unui sir -> alt sir
# folosim concatenare de felii - pentru modificari legate de pozitie
# exemplu - stergerea elementului de pe pozitia k
s = "un sir"
k = 2
s = s[:k] + s[k + 1:]
print(s)

# replace(old, new, count) - inlocuieste un subsir cu alt subsir;
# param. count e optional, altfel sunt inlocuite toate aparitiile
s = "acesta acela"
s = s.replace("a", "", 2)
print(s)

# transformari la nivel de caracter: lower(), upper(), title()
s = s.upper()
print(s)
# testare - islower(), isupper(), isdigit(), isalnum() => True/False

# Divizare, unificare
# split(separator, maxsplit) - separator e optional; imparte sirul folosind ca delimitator separator;
# implicit se folosesc caracterele albe
# !!! se poate transmite doar un singur separator ca parametru
# returneaza o lista cu cuvintele din sir
prop = "aceasta, este o propozitie"
ls = prop.split()
print(ls)

# putem transmite metodei split si un parametru maxsplit; lista returnata va avea cel mult maxsplit+1 elem
ls1 = prop.split(maxsplit=2)
print(ls1)

# !!! mai exista si rsplit, de la dreapta la stanga

# pentru a concatena elementele unei liste de cuvinte folosind un delimitator dat
# se poate folosi metoda join: delimitator.join(lista)
s = ",".join(ls)
print(s)

ls = sorted("pauza")
print(ls)
s = "".join(ls)
print(s)

# f-stringuri - siruri de formatare -> pot contine nume de variabile sau expresii
x = "ab"
y = "abcde"
s = f"{x} este un subsir al lui {y}"
print(s)
x = 8
y = 3
# 8 + 3 = 3 + 8 = 11
print(f'{x} + {y} = {y} + {x} = {x + y}')

x = 1.1 + 2.2
print(f'{x}')
print(f'{x:f}')
print(f'{x:.2f}')
x = 9
print(f'{x:4b}')  # poate trb python mai nou
print(f'{x:016b}')  #spatiul ramas se umple cu 0

