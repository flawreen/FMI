"""
Fișierul text cinema.in conține programul dintr-o zi al unui lanț de cinematografe. Fiecare linie
din fișier are următoarea structură:
nume_cinematograf % nume_film % ore_de_difuzare
unde nume_cinematograf este un șir de caractere reprezentând numele unui cinematograf,
nume_film este numele unui film (numele cinematografului și al filmului sunt formate din cuvinte
separate prin câte un spațiu și nu conțin caracterul '%'), iar ore_de_difuzare este un șir de
caractere conținând orele (sub forma hh:mm) la care este programat filmul în cinematograf, orele
fiind separate prin câte un spațiu. Un exemplu de astfel de fișier este:

cinema.in
Cinema 1 % Minionii 2 % 12:30 18:30
Cinema 3 % Elfii cofetari % 10:30 12:30
Cinema 2 % Minionii 2 % 15:00 18:30 20:30
Cinema 1 % Elfii cofetari % 10:00 12:30
Cinema 2 % Gasca Animalutelor % 15:00 18:30 20:00
Cinema 4 % Minionii 2 % 16:00 18:30 20:30
Cinema 1 % Buna dimineata % 09:30

a) [2,5 p.] Să se memoreze datele din fișier într-o singură structură de date astfel încât să se
răspundă cât mai eficient la cerințele de la punctele următoare.
"""
cinema = {}
with open("files/cinema.in", "r") as f:
    for linie in f:
        ls = linie.rstrip("\n").split(" % ")
        if ls[0] not in cinema:
            cinema[ls[0]] = {}
        cinema[ls[0]][ls[1]] = set(ls[2].split())
"""
b) [1 p.] Scrieți o funcție sterge_ore care are următorii parametri (în această ordine):
• structura în care s-au memorat datele la cerința a)
• un șir de caractere cinema reprezentând numele unui cinematograf
• un șir de caractere film reprezentând numele unui film
• mulțime ore având ca elemente șiruri de caractere de forma hh:mm
Funcția va șterge din programul cinematografului cinema programările filmului film de la
orele din mulțimea ore și va returna o listă cu filmele programate la cinematograful cinema după
această actualizare. 
Se citesc de la tastatură un nume de film f, un nume de cinematograf c și un
șir de caractere o de forma hh:mm reprezentând o oră. Să se apeleze funcția sterge_ore pentru
a șterge programarea filmului f la cinematograful c la ora o și să se afișeze lista returnată; după
apelul funcției să se afișeze și structura în care s-au memorat datele.
"""
def sterge_ore(data, nume, film, ore):
    if nume in data and film in data[nume]:
        for x in ore:
            data[nume][film].discard(x)

        if len(data[nume][film]) == 0:
            del data[nume][film]
            if len(data[nume]) == 0:
                del data[nume]
            return []
        return list(data[nume].keys())
    return []
# c, f, o = input(), input(), [x for x in input().split()]
# print(sterge_ore(cinema, c, f, o))
# print(cinema)
"""
c) [1,5 p.] Scrieți o funcție cinema_film care primește următorii parametri: structura în care s-
au memorat datele la cerința a), un număr variabil de șiruri de caractere reprezentând nume
de cinematografe și doi parametri ora_minima și ora_maxima șiruri de caractere de forma
“hh:mm” reprezentând ore. Funcția returnează o listă de tupluri cu elementele de tip
(nume_film, nume_cinema, lista_de_ore) cu filmele care rulează (încep) la cel puțin unul
dintre cinematografele primite ca parametru între orele ora_minima și ora_maxima, unde:
• nume_film este numele unui astfel de film
• nume_cinema este un nume de cinema dintre cele primite ca parametru la care rulează
filmul nume_film
• lista_de_ore este lista orelor la care este programat filmul nume_film la cinematograful
nume_cinema între orele ora_minima și ora_maxima, ordonată crescător

Lista returnată va fi ordonată crescător după numele filmului, apoi, în caz de egalitate,
descrescător după numărul de elemente din lista_de_ore. 

Să se apeleze funcția pentru cinematografele ‘Cinema 1’ și ‘Cinema 2’, ora_minima "14:00" și ora_maxima "22:00" și să se afișeze lista returnată. 

Explicații: pentru datele din fișier lista returnată va fi [('Gasca
Animalutelor', 'Cinema 2', ['15:00', '18:30', '20:00']), ('Minionii 2', 'Cinema 2', ['15:00', '18:30',
'20:30']), ('Minionii 2', 'Cinema 1', ['18:30'])]; filmul ‘Elfii cofetari’ nu apare în listă deoarece este
programat mai devreme de ora “14:00”.
"""

def cinema_film(data, *nume, ora_minima, ora_maxima):
    ls = []
    for nume_cinema in nume:
        for film in data[nume_cinema]:
            lista_ore = [x for x in data[nume_cinema][film] if ora_minima <= x <= ora_maxima]
            if len(lista_ore) > 0:
                lista_ore.sort()
                ls.append((film, nume_cinema, lista_ore))
    ls.sort(key=lambda x: (x[0], -len(x[2])))  # trebuie sa fac tuplu pt sortare dupa mai multi parametri cu lambda
    # ls.sort(key=lambda x: len(x[2]), reverse=True)
    return ls

print(*cinema_film(cinema, "Cinema 1", "Cinema 2", ora_minima="14:00", ora_maxima="22:00"))

