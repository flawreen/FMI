def apartine(multime, *ls):
	d = {}
	for nr in multime:
		d[nr] = list()
		i = 0
		for lista in ls:
			frecv = lista.count(nr)
			if frecv > 0:
				d[nr].append((i, frecv))
			i += 1
	return d


# a)
print(apartine({10, 20}, [10, 11, 10], [20, 20, 40], [5], [10, 11]))
# b)
perechi = [(a, b) for a in range(1, 11) for b in range(1, 11) if a < b]
print(perechi)
# c) O(log n)

