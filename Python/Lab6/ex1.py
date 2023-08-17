"""1.Subsecvența de sumă maximă a unui șir: Se dă un șir de numere(în fișier, separate prin spații). Să se afișeze
o subsecvenţă de sumă maximă a șirului (formată cu elemente consecutive) O(n)
date.in
1 -2 3 -1 5 2 -6 1 3
date.out
3 -1 5 2
Indicație: Subproblema s[i] = subsecvența de sumă maxima care se termină pe poziția i
Recurența:s[i] = max{s[i-1]+v[i], v[i]} (unde v este șiruldat) – deoarece
subsecvența care se termină pe poziția i este formată din elementul v[i] la
care se adaugă eventual subsevența care se termină pe poziția i-1 (daca astfel se obține o suma mai mare) """
with open("files/date.in") as f:
	ls = [int(x) for x in f.readline().split()]

lung = len(ls)
suma = [ls[0]]
succ = [-1 for _ in range(lung)]
succ[0] = 0
sumMax = None
imax = None

for i in range(1, lung):
	if ls[i] + suma[i-1] > ls[i]:
		suma.append(suma[i-1] + ls[i])
	else:
		suma.append(ls[i])

	if sumMax is None:
		sumMax = suma[-1]
	elif sumMax < suma[-1]:
		sumMax = suma[-1]
		imax = i  # retin ultimul indice pe care se gaseste val max

	if ls[i] + suma[i-1] == suma[i]:
		succ[i] = succ[i-1]
	else:
		succ[i] = i

print(ls[succ[imax]:imax+1])
