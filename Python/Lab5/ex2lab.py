"""
2. a) Scrieți o funcție cu număr variabil de parametri care să furnizeze numărul natural obținut
prin alipirea cifrelor maxime ale numerelor naturale nenule primite ca parametri.
De exemplu, pentru numerele 4251, 73, 8 și 133 funcția trebuie să returneze numărul 5783.
"""
def nrmax(*args):
    sol = 0
    for x in args:
        cifmax = 0
        while x > 0:
            if x % 10 > cifmax:
                cifmax = x%10
            x //= 10
        sol = sol*10 + cifmax
    return sol
"""
b) Scrieți o funcție cu 3 parametri nenuli de tip întreg a,b și c care să verifice dacă aceștia pot
fi considerați ca fiind numere scrise în baza 2 sau nu, folosind apeluri utile ale funcției definite
anterior. De exemplu, pentru numerele 1001, 11 și 100 funcția trebuie să returneze valoarea
True, iar pentru numerele 1001, 17 și 100 trebuie să returneze valoarea False.
"""
def verifbin(a, b, c):
    if nrmax(a, b) > 11:
        return False
    if nrmax(a, c) > 11:
        return False
    return True
print(verifbin(1001, 17, 100))



