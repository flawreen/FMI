def bkt(k):
	global n, div, x
	for i in range(2, n):
		x[k] = i
		if prim(x[k]) and x[k] >= x[k-1] and sum(x[1:k]) <= n:
			if sum(x[1:k+1]) == n:
				print(x[1:k+1])
			else:
				bkt(k+1)


n = int(input())
div = []
def prim(i):
	if i == 2 or i == 3:
		return True
	for d in range(2, i//2+1):
		if i % d == 0:
			return False
	else:
		return True
x = [0 for _ in range(n+1)]
bkt(1)
