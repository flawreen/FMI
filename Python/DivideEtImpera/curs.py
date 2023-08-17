"""
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$    ###############################################  $
$   #  la consultatie se rasp la intrebari	        #   $
$ #   27 -> consultatie la facultate 12 - 16          #   $
$   #  28 -> consultatie online 11 - 16 oricand     #   $
$    ##############################################   $
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$



Progr. dinamica

# Pb rucsacului -> var discreta (obiectele nu se pot fractiona)
intrare:
G -> nr nat. -> capacitatea rucsacului
n obiecte -> pt fiecare obiect i --> greutatea gi nr nat
							   |
							   ----> castigul Gi
iesire:
Ob. incarcate in rucsac a.i:
- castigul total - maxim
- cant totala <= G

Exc:
G = 9
ob g: 6 3 4 4
c: 5 3 5 5
sol opt = {ob 3, ob 4}

Solutie:
				 1  2  3  4
-> de forma x = (Nu Nu Da Da)
    			 0  0  1  1
Decizie -> Cum pot decide dc iau ult ob sau nu
|======> il iau -> raman cu ob. {1, ..., n-1} si greutatea G - gn
|			Castigul in acest caz va fi
| 			cn + castigul total pt ob {1, ..., n-1} si greutatea G - gn (subpb)
|
|
|======> nu il iau -> pb se reduce la ob {1, ..., n-1} si greutatea G
			Castigul in acest caz va fi
			castigul total pt ob {1, ..., n-1} si gr G (subpb)

Subpb:
+	s[i][g] = castigul maxim pt ob {1, ..., i} si greutatea g <= G

Sol. pb:
+	s[n][G]

Rel. de recurenta:
		  {
		  | max{ci + s[i-1][g-gi], s[i-1][g]}, daca g <= gi  (adica ob incape in rucsac)
		  |		il iau			 nu il iau
s[i][j] = |
		  | s[i-1][g]						   , altfel
		  {

Stim:
+ 	s[0][g] = 0  (sunt 0 obiecte)
+ 	s[i][0] = 0
in implementare g este gr
"""
f = open("files/rucsac.in")
G = int(f.readline())
n = int(f.readline())
v = [int(x) for x in f.readline().split()]
g = [0] + v  # obiectele indexate de la 1 la n

c = [int(x) for x in f.readline().split()]
c = [0] + c
print(g, c, sep="\n")
f.close()
s = [[0 for g in range(G+1)] for i in range(n+1)]

# avem deja s[i][0] = 0 si s[0][g] = 0
for i in range(1, n+1):
	for gr in range(1, G+1):
		if g[i] <= gr:  # obiectul incape in rucsac
			s[i][gr] = max(c[i] + s[i-1][gr - g[i]], s[i-1][gr])  # max(iau, nu iau ob i)
		else:
			s[i][gr] = s[i-1][gr]
for linie in s:
	print(*linie)
print(s[n][G])

# varianta dde afisare obiecte - mergem inapoi pe relatia de recurenta
i = n
gr = G
while i > 0 and gr > 0:
	if g[i] <= gr and s[i][gr] == c[i] + s[i-1][gr - g[i]]:  # am luat ob i
		print(i, end=" ")  # se reduce la subpb: i-1 ob, greutatea gr - g[i]
		i -= 1
		gr -= g[i]
	else:
		i -= 1


def afis(i, ggr):  # varianta recursiva
	if i > 0 and ggr > 0:
		if g[i] <= ggr and s[i][ggr] == c[i] + s[i-1][ggr - g[i]]:
			afis(i-1, ggr - g[i])
			print(i, end=" ")
		else:
			afis(i-1, ggr)


afis(n, 6)

