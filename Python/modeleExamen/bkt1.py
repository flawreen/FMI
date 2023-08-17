def bkt(k):
	global S, n, x
	for i in range(0, 21):
		x[k] = i
		if sum([x[i] * v[i] for i in range(1, k)]) <= S:
			if k == n and sum([x[i] * v[i] for i in range(1, n+1)]) == S:
				print(x[1:])
			else:
				if k < n:
					bkt(k+1)


S = 20
n = 3
v = [0, 1, 5, 10]
x = [0, 0, 0, 0]
bkt(1)
