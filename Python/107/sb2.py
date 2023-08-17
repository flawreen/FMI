n = int(input())
betisoare = list()
solutia = []
d = {}
for i in range(n):
	x = [int(x) for x in input().split()]
	betisoare.append((x[0], x[1]))
	d[(x[0], x[1])] = i+1

betisoare.sort(key=lambda x: x[1])
solutia.append(betisoare[0])
rez = []
for i in range(1, n):
	if betisoare[i][0] <= solutia[-1][1]:
		rez.append(d[betisoare[i]])
	else:
		solutia.append(betisoare[i])
rez.sort()
print(" ".join([str(x) for x in rez]))
"""
5
3 70
1 9
1 19
11 20
40 40

In algoritmul de mai sus am citit intr-o lista capetele fiecarui betisor sub forma de tuplu si am adaugat intr-un 
dictionar indexul tuplului. Apoi am sortat lista dupa capatul din dreapta al betisorului, si am adaugat primul 
element in lista solutia, unde se afla betisoarele care nu isi intersecteaza capetele. Apoi, intr-un for am adaugat 
betisoarele al caror capat stang nu se intersecteaza cu capatul drept al ultimului betisor adaugat in lista solutia, 
iar cele al caror capat stang se intersecteaza le-am adaugat index-ul inainte de sortare in lista rez. Dupa for am 
sortat lista rez crescator si am afisat elementele cu spatiu intre ele.
Se incadreaza in metoda Greedy deoarece am sortat lista cu capetele betisoarelor crescator in functie de capatul 
stang, astfel incat cand parcurg vectorul de la al doilea element spre ultimul, voi putea adauga betisoarele cu cel 
mai mic capat drept dar cu capatul stang neintersectat cu betisorul anterior adaugat la solutie.
Criteriul este corect deoarece, datorita sortarii crescatoare dupa capatul drept al fiecarui betisor, la parcurgerea 
listei betisoarele consecutive vor fi cele care au capatul drept mai mic decat urmatoarele din lista. In plus, 
in structura repetitiva selectez betisorul i din betisoare care nu se intersecteaza betisorul h din solutia. Astfel, 
raman betisoarele neselectate, care sunt in numar minim datorita solutiei optime de selectare a betisoarelor.
"""
