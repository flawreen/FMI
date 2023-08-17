"""
a) [2,5 p.] Să se memoreze datele din fișier într-o singură structură de date astfel încât să se
răspundă cât mai eficient la cerințele de la punctele următoare.
cinema.in
Cinema 1 % Minionii 2 % 12:30 18:30
Cinema 3 % Elfii cofetari % 10:30 12:30
Cinema 2 % Minionii 2 % 15:00 18:30 20:30
Cinema 1 % Elfii cofetari % 10:00 12:30
Cinema 2 % Gasca Animalutelor % 15:00 18:30 20:00
Cinema 4 % Minionii 2 % 16:00 18:30 20:30
Cinema 1 % Buna dimineata % 09:30
4:02 - 4:18"""
with open("cinema.in") as f:
	d = {}
	for linie in f:
		s = linie.rstrip('\n').split(" % ")
		d.setdefault(s[0], dict())
		d[s[0]].setdefault(s[1], set())
		ls = s[2].split()
		for x in ls:
			d[s[0]][s[1]].add(x)

"""
b) [1 p.] Scrieți o funcție sterge_ore care are următorii parametri (în această ordine):
• structura în care s-au memorat datele la cerința a)
• un șir de caractere cinema reprezentând numele unui cinematograf
• un șir de caractere film reprezentând numele unui film
• mulțime ore având ca elemente șiruri de caractere de forma hh:mm
Funcția va șterge din programul cinematografului cinema programările filmului film de la
orele din mulțimea ore și va returna o listă cu filmele programate la cinematograful cinema după
această actualizare. 

Se citesc de la tastatură un nume de film f, un nume de cinematograf c și un șir de caractere o de forma hh:mm 
reprezentând o oră. Să se apeleze funcția sterge_ore pentru a șterge programarea filmului f la cinematograful c la 
ora o și să se afișeze lista returnată; după apelul funcției să se afișeze și structura în care s-au memorat datele. 
4:19 - 4:40"""


def sterge_ore(date, nume_cinema, nume_film, *ore):
	for y in ore:
		date[nume_cinema][nume_film].discard(y)
	if len(date[nume_cinema][nume_film]) == 0:
		del date[nume_cinema][nume_film]
	return list(date[nume_cinema].keys())


# f, c, o = input(), input(), input()
# print(sterge_ore(d, c, f, o))
# print(d)
"""
c) [1,5 p.] Scrieți o funcție cinema_film care primește următorii parametri: structura în care s-
au memorat datele la cerința a), un număr variabil de șiruri de caractere reprezentând nume
de cinematografe și doi parametri ora_minima și ora_maxima șiruri de caractere de forma
“hh:mm” reprezentând ore. 

Funcția returnează o listă de tupluri cu elementele de tip
(nume_film, nume_cinema, lista_de_ore) cu filmele care rulează (încep) la cel puțin unul
dintre cinematografele primite ca parametru între orele ora_minima și ora_maxima, unde:
• nume_film este numele unui astfel de film
• nume_cinema este un nume de cinema dintre cele primite ca parametru la care rulează
filmul nume_film
• lista_de_ore este lista orelor la care este programat filmul nume_film la cinematograful
nume_cinema între orele ora_minima și ora_maxima, ordonată crescător

Lista returnată va fi ordonată crescător după numele filmului, apoi, în caz de egalitate,
descrescător după numărul de elemente din lista_de_ore. 

Să se apeleze funcția pentru
cinematografele ‘Cinema 1’ și ‘Cinema 2’, ora_minima "14:00" și ora_maxima "22:00" și să se
afișeze lista returnată. 

Explicații: pentru datele din fișier lista returnată va fi [('Gasca
Animalutelor', 'Cinema 2', ['15:00', '18:30', '20:00']), ('Minionii 2', 'Cinema 2', ['15:00', '18:30',
'20:30']), ('Minionii 2', 'Cinema 1', ['18:30'])]; filmul ‘Elfii cofetari’ nu apare în listă deoarece este
programat mai devreme de ora “14:00”.
4:41 - 4:53"""


def cinema_film(date, *nume_cinema, ora_minima=None, ora_maxima=None):
	rez = []
	for cinema in nume_cinema:
		for filme in date[cinema]:
			ore = [ora for ora in date[cinema][filme] if ora_minima <= ora <= ora_maxima]
			if len(ore) > 0:
				ore.sort()
				rez.append((filme, cinema, ore))
	rez.sort(key=lambda a: (a[0], -len(a[2])))
	return rez


o1 = "14:00"
o2 = "22:00"
ls = cinema_film(d, 'Cinema 1', 'Cinema 2', ora_minima=o1, ora_maxima=o2)
print(ls)
