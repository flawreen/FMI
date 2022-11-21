"""
2. Din fișierul studenti.in se citesc, de pe câte o linie, date despre câte un student, astfel:
Nume, Prenume, grupa, nota1, nota2, .... (numărul de note poate varia între 0 si 5,
deoarece în sesiune sunt 5 examene și la unele examene studentul poate fi absent).
a) Să se afișeze pentru fiecare grupă în parte studenții;

b) Să se afișeze pentru o grupă citită de la tastatură numele și media fiecărui student dacă a
fost prezent și a promovat toate cele 5 examene din sesiune sau mesajul "restantier"

c) Pentru o eventuală repartizare a locurilor de cazare, să se afișeze toți studenții ordonați
astfel:
- mai întâi integraliștii ordonați după medie descrescător;
- restanțierii ordonați după numărul de restanțe crescător.

Exemplu de fișier de intrare:
Petre, Ana, 191, 9, 10, 8, 8, 5
Marin, Ioana, 191, 5, 10, 10, 7, 8
Popescu, Maria, 191, 10, 10, 10
Marin, Ioana, 191, 5, 4, 5, 8, 8
Zaru, Anton, 191, 10, 10, 8, 8, 9
Petrecu, Mircea, 192, 10, 10, 10, 10, 10

La punctul b pentru grupa 191 se va afișa
Petre Ana 8.0
Marin Ioana restantier
Popescu Maria restantier
Zaru Anton 9.0

La punctul c se va afișa
Petrecu Mircea media 10.0
Zaru Anton media 9.0
Petre Ana media 8.0
Marin Ioana restante 1
Popescu Maria restante 2
"""
f = open("files/studenti.in")
d = {}
for linie in f:
    ls = linie.rstrip("\n").split(", ")
    nume = ls[0] + " " + ls[1]
    grupa = int(ls[2])
    note = [int(x) for x in ls[3:]]

    # cream dictionarul de dictionare
    if grupa in d:
        d[grupa][nume] = note
    else:
        d.setdefault(grupa, {nume: note})

print("a)")
for grupa in d:  # dupa chei
    print(grupa)
    # print(*sorted(d[grupa].keys()), sep="\n")  # pentru afisarea studentilor doar
    for nume in d[grupa]:
        print(nume, *d[grupa][nume])

print("b)")
grupa = 191
for nume in d[grupa]:
    ls_note = d[grupa][nume]
    if len(ls_note) == 5 and min(ls_note) >= 5:
        md = sum(ls_note) / len(ls_note)
        print(f"{nume} media {md:.2f}")
    else:

        print(f"{nume} restantier")

print("c)")
integralisti = {}
restantieri = {}
for nume in d[grupa]:
    ls_note = d[grupa][nume]
    if len(ls_note) == 5 and min(ls_note) >= 5:
        media = sum(ls_note) / len(ls_note)
        integralisti.setdefault(media, nume)
    else:
        if len(ls_note) == 5:
            nr_restante = len([x for x in d[grupa][nume] if x < 5])
        else:
            nr_restante = 5 - len(ls_note)
        restantieri.setdefault(nr_restante, nume)

note = list(integralisti.keys())
restante = list(restantieri.keys())
note.sort(reverse=True)
restante.sort()
for nota in note:
    print(f"{integralisti[nota]} media {nota:.2f}")
for restanta in restante:
    print(f"{restantieri[restanta]} restante {restanta}")



