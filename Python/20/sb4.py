def bkt(k):
	global n, t, x, counter
	for i in range(1, t+1):
		x[k] = i
		if ((k > 1 and x[k] <= x[k-1]) or (k == 1)) and sum(x[1:k]) <= n:
			if sum(x[1:k+1]) == n:
				print(x[1:k+1])
				counter += 1
			else:
				if k < n:
					bkt(k+1)


n, t = int(input()), int(input())
counter = 0
x = [0 for _ in range(n+1)]
bkt(1)
print(counter)
