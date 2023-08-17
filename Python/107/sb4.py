def bkt(k):
	global n, s, x, exista
	for i in range(1, 9):
		x[k] = i
		if sum(x[1:k]) <= s and x[k] >= x[k-1]:
			if k == n and sum(x[1:]) == s:
				print("".join([str(x) for x in x[1:]]))
				exista = 1
			else:
				if k < n:
					bkt(k+1)


n = int(input())
s = int(input())
x = [0 for _ in range(n+1)]
exista = 0
bkt(1)


