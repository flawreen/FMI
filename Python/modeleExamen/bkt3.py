def bkt(k):
	global n, a, p, x, v
	for i in range(1, n+1):
		x[k] = i
		if x[k] > x[k-1] and sum([v[j] for j in x[1:k]]) <= p:
			if k == a and sum([v[j] for j in x[1:a+1]]) == p:
				print(x[1:])
			elif k < a:
				bkt(k+1)


n, a, p = [int(x) for x in input().split()]
x = [0 for _ in range(a+1)]
v = [0] + [int(c) for c in input().split()]
bkt(1)
