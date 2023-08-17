"""
2. Scrieți o funcție nr_aparitii cu complexitate O(log(n)) care primește ca parametru o listă de numere
întregi ordonată crescător și un număr x și returnează numărul de apariții ale unei valori x în listă.
De exemplu, nr_aparitii( [1, 1, 2, 2, 2, 2, 6, 9, 9, 20], 2) va returna 4.

pt if v[m] == x varianta non O(logn)
k = m+1
while v[m] == x and m >= 0:
	m -= 1
	nr_ap += 1
while v[k] == x and k < n:
	k += 1
	nr_ap += 1
break
"""


def caut(v, ls, ld, x):
	if ls > ld:
		return -1
	m = (ls + ld) // 2
	if v[m] != x:
		return m
	elif v[m] > x:
		caut(v, ls, m-1, x)
	else:
		caut(v, m+1, ld, x)


def nr_aparitii(v, x):
	n = len(v)
	ls = 0
	ld = n-1
	nr_ap = 0
	while ls < ld:
		m = (ls+ld) // 2
		if v[m] == x:
			i = caut(v, 0, m - 1, x)
			j = caut(v, m, ld, x)
			return i, j
		elif v[m] > x:
			ld = m-1
		else:
			ls = m+1


i, j = nr_aparitii([1, 1, 2, 2, 2, 2, 6, 9, 9, 20], 2)
i += 1
print(j-i)
