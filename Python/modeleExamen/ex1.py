"""
a) [0.5 p.] Scrieți o funcție citire_numere cu un parametru reprezentând numele unui fișier text
care conține, pe mai multe linii, numere naturale despărțite între ele prin spații și returnează o
listă de liste (numite subliste), elementele unei subliste fiind numerele de pe o linie din fișier.
3:31 - 3:31"""


def citire_numere(nume):
	with open(nume) as f:
		ls = [[int(x) for x in linie.split()] for linie in f]
	return ls


"""
b) [2 p.] Să se scrie o funcție prelucrare_lista care primește ca parametru o listă de liste pe care
o modifică astfel:
• din fiecare sublistă se vor elimina toate aparițiile valorii minime, apoi
• din fiecare sublistă se vor păstra doar primele m elemente, unde m reprezintă lungimea
minimă a unei subliste.
3:32 - 3:44"""


def prelucrare_lista(ls):
	lungime_minima = len(ls[0])
	for linie in ls:
		minim = min(linie)
		while True:
			try:
				linie.remove(minim)
			except ValueError:
				break
		if len(linie) < lungime_minima:
			lungime_minima = len(linie)
	for i in range(len(ls)):
		ls[i][:] = ls[i][:lungime_minima]


"""
c) [0.5 p.] Se dă fișierul "numere.in" cu următoarea structură: pe linia 𝑖 se află separate prin câte
un spațiu 𝑛 numere naturale reprezentând elementele de pe linia 𝑖 a unei matrice, ca în exemplul
de mai jos. Să se apeleze funcția prelucrare_lista pentru matricea obținută în urma apelului
funcției citire_numere pentru fișierul text numere.in. Matricea astfel obținută să se afișeze pe
ecran, fără paranteze și virgule, iar elementele de pe fiecare linie să fie separate prin câte un
spațiu.
3:44 - 3:47"""
mat = citire_numere("numere.in")
prelucrare_lista(mat)
print("\n".join([" ".join([str(x) for x in linie]) for linie in mat]))

"""
d) [1 p.] Fie L matricea (memorată ca listă de liste) obținută în urma apelării funcției citire_numere
pentru fișierul text "numere.in". Să se citească de la tastatură un număr natural nenul k și apoi
să se scrie în fișierul text "cifre.out" elementele matricei L care sunt formate din exact k cifre sau
mesajul “Imposibil!” dacă nu există niciun element cu proprietatea cerută. Elementele vor fi
scrise în fișier în ordine descrescătoare și fără duplicate.
3:47-3:56"""
mat = citire_numere("numere.in")
k = int(input())
with open("citire.out", "w") as g:
	rez = [x for linie in mat for x in linie if 10**(k-1) <= x < 10**k]
	if len(rez) == 0:
		g.write("Imposibil!")
	else:
		rez = list(set(rez))
		rez.sort(reverse=True)
		g.write(" ".join(str(x) for x in rez))

# Total: 25 min
