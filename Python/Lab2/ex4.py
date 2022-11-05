propoz = input()
s = input()
t = input()
p = int(input("numarul de greseli de corectat: "))
if propoz.count(t) > p:
    propoz = propoz.replace(t, s, p)
    print(f'mai mult de {p} greseli')
else:
    propoz = propoz.replace(t, s, p)
print(propoz)
