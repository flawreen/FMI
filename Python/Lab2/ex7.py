"""
7. Se citește de la tastatură un text. Se cere să se “traducă” în limba păsărească textul dat
astfel: după fiecare vocală se adaugă litera p și încă o dată acea vocală (după a, e, i, o,
u se adaugă respectiv pa, pe, pi, po, pu). Exemplu: “Ana are mere.” devine “Apanapa
aparepe meperepe.” """

text = input("text: ")
aeiou = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
vocale = {v: f'{v}p{v.lower()}' for v in aeiou}
rez = []

for s in text:
    if s in aeiou:
        rez.append(vocale[s])
    else:
        rez.append(s)

rez = "".join(rez)
print(rez)
print(vocale)

"""
Fiind dat un astfel de text în limba păsărească, se poate obține
textul original? Dacă da, scrieți un program care primind un text în limba păsărească
construiește în memorie și afișează textul inițial.

text = input("text: ")
aeiou = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
pasareasca = ['apa', 'epe', 'ipi', 'opo', 'upu', 'Apa', 'Epe', 'Ipi', 'Opo', 'Upu']
vocale = {f'{v}p{v.lower()}': v for v in aeiou}
rez = []

for p in pasareasca:
    lastpoz = poz = 0
    poz = text.find(p, poz)
    while poz != -1:
        text = text[:poz] + vocale[p] + text[poz + 3:]
        lastpoz = poz + 3
        poz = text.find(p, poz + 1)

print(text)"""
