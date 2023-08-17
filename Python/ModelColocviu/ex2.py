"""
Complexitatea maximă a soluției: O(nlog2 n )
Considerăm n spectacole S1, S2, ..., Sn pentru care cunoaștem intervalele lor de desfășurare
[s1, f1), ..., [sn, fn), toate dintr-o singură zi. Având la dispoziție o singură sală, în care putem
să planificăm un singur spectacol la un moment dat, să se determine numărul maxim de
spectacole care pot fi planificate fără suprapuneri. Un spectacol Sj poate fi programat
după spectacolul Si dacă sj ≥ fi. Justificați corectitudinea programului și complexitatea sa.
9:00
program: 9:15
argumentare + descriere: 9:28
semnif. var: 9:30
justif: 9:37
complex: 9:42

42 minute
"""
n = int(input())
spectacole = []  # lista in care stochez input-ul
sol = []  # lista in care voi stoca elementele ce fac parte din solutia optima
rez = 0  # numarul de spectacole care pot fi planificate fara suprapuneri
for _ in range(n):  # O(n)
	ls = input().lstrip('[').rstrip(')').split(", ")  # lista provizorie din care preiau doar numerele
	spectacole.append((int(ls[0]), int(ls[1])))
spectacole.sort(key=lambda x: x[1])  # (O(nlog2 n)
sol.append(spectacole[0])
rez += 1
for i in range(1, len(spectacole)):  # O(n-1)
	if spectacole[i][0] > sol[-1][1]:
		sol.append(spectacole[i])
		rez += 1
print(rez)
"""
Algoritmul scris mai sus foloseste o lista pentru a stoca input-ul si o lista pentru spectacolele ce fac parte din 
solutie. Primul for este pentru a prelua numerele de input sub forma de tuplu, care apoi e adaugat in lista de 
spectacole. Apoi, am sortat lista cu spectacole dupa timpul de terminare, pentru a evalua pe rand, in mod Greedy, 
spectacolele ce se termina cel mai rapid, astfel incat sa pot programa cat mai multe spectacole. 

In al doilea for, incepand cu al doilea element, deoarece primul element este deja parte din solutie datorita 
sortarii, am adaugat la solutie primul spectacol din lista care incepe cel mai devreme, dar mai tarziu decat timpul 
de terminare al ultimului spectacol adaugat la solutie, si am contorizat de cate ori se intampla acest lucru.

Astfel, metoda se incadreaza in metoda Greedy, avand in vedere faptul ca am sorta lista cu spectacole crescator dupa 
timpul de terminare si am adaugat la solutie spectacolele cu cel mai mic timp de incepere si in acelasi timp mai mare 
decat timpul de terminare al ultimului spectacol din lista de solutii.

Adaugarea spectacolelor care incep cel mai devreme si mai tarziu decat ultimul spectacol adaugat la solutia optima si 
sortarea listei cu spectacolele crescator dupa timpul de terminare sunt corecte deoarece, in acest fel, 
spectacolele adaugate la solutia optima vor fi cele care se termina cel mai devreme si care nu se suprapun, 
spre deosebire de cazul incare ar fi fost sortate crescator dupa timpul de incepere, in acest fel daca activitatea 
care incepea cel mai devreme si se termina cel mai tarziu era adaugata la solutie, ar fi fost singura activitate.

Complexitatea solutiei propuse este de O(nlog2 n), deoarece citirea lui n, initializarea listelor si variabilei au 
complexitate O(1), primul for are complexitatea O(n) din cauza metodei split, sortarea listei spectacole are 
complexitatea O(nlog2 n), iar cel de-al doilea for este O(n-1) deoarece parcurg vectorul de la al doilea la ultimul 
element, si in if ambele comenzi sunt O(1)
"""
