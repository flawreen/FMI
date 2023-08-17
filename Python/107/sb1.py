def frecvente(*liste):
	d = dict()
	p = dict()
	for ls in liste:
		for x in ls:
			p.setdefault(x, 0)
			p[x] += 1
	for nr in p:
		d.setdefault(p[nr], list())
		d[p[nr]].append(nr)
	return d


print(frecvente([20, 10, 40, 20], [10, 20, 10], [40, 30, 40]))
# b)
tupluri = [(x, x//6, x % 6) for x in range(1, 21) if x//6 != x % 6]
print(tupluri)



