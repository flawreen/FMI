def bkt(k):
	global c, x, p, exista
	for i in range(1, c+1):
		x[k] = i
		if sum(x[1:k]) <= c:
			if sum(x[1:k+1]) == c and max(x[1:k+1]) - min(x[1:k+1]) <= p:
				print("".join(str(x) for x in x[1:k+1]))
				exista = 1
			else:
				if k < c:
					bkt(k+1)


p, c = 3, 6
x = [0 for _ in range(c+1)]
exista = 0
bkt(1)
if exista == 0:
	print("Nu exista")

