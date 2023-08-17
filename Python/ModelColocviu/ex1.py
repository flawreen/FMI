"""
a) Scrieți o funcție divizori care primește un număr variabil de parametri numere
naturale și returnează pentru fiecare număr primit ca parametru lista divizorilor săi
primi sub forma unui dicționar cu perechi de forma număr: lista divizorilor. De exemplu,
pentru apelul divizori(50, 21) funcția trebuie să furnizeze dicționarul {50: [2,5], 21: [3,7]}.
(1.5 p.)
8:32 - 8:43 => 11 min
"""


def divizori(*ls):
	diviz = {}
	for nr in ls:
		diviz[nr] = []
		for i in range(2, nr // 2 + 1):
			if nr % i != 0:
				continue

			if i == 2 or i == 3:
				diviz[nr].append(i)
			else:
				for j in range(2, i // 2 + 1):
					if i % j == 0:
						break
				else:
					diviz[nr].append(i)
	return diviz


print(divizori(50, 21))
"""
b) Înlocuiți punctele de suspensie din instrucțiunea litere_10 = [...] cu o expresie astfel
încât lista să fie inițializată cu primele 10 litere mici din alfabetul englez. (0.5 p.)
2 min
"""
litere_10 = [chr(s) for s in range(ord('a'), ord('a') + 10)]
print(litere_10)


