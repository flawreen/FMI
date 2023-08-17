def bkt(k):
	global d, m, x, exista
	for i in range(1, d+m+1):
		x[k] = i
		if x[k] not in x[1:k] and (x[k] <= d or (x[k] > d >= x[k-1])):
			if k == d+m and x[1] <= d and x[-1] <= d:
				print(x[1:])
				exista = 1
			else:
				if k < d+m:
					bkt(k+1)


d = int(input())
m = int(input())
exista = 0
x = [0 for _ in range(d+m+1)]
bkt(1)
