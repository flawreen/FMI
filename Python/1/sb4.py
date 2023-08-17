def bkt(k):  # k=indicele componentei curente(xk)
	# uneori va fi nevoie de global n, x
	global n, x, corturi, m
	for v in range(1, n):  # (1)  trecerea pe verticala    v este variabila locala, forul stie mereu unde a
		# ramas
		x[k] = v
		if k <= m and x[k] <= corturi[k]:  # (2)
			if k == m and sum(x[1:k+1]) == n and x[1] == corturi[1]:  # (3)  trecerea orizontala pe DREAPTA
				print(x[1:m+1])
			else:
				bkt(k+1)


n = int(input())
m = int(input())
corturi = [int(x) for x in input().split()]
corturi = [0] + corturi
x = [0 for _ in range(n+1)]
bkt(1)
"""
9
3
5 2 4
"""
