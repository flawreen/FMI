import bisect


def maxPairs(skillLevel, minDiff):
	if minDiff == 0:
		return
	skillLevel.sort()
	ls = skillLevel
	counter = 0
	used = []
	for i in range(len(ls)-1, -1, -1):
		m = i
		n = 0
		if i in used:
			continue
		while n < m:
			mijl = (n+m)//2
			if ls[mijl] <= ls[i]-minDiff:
				k, l = n+1, m
				while k < l:
					mijl2 = (k+l)//2
					if ls[mijl] <= ls[mijl2] <= ls[i]-minDiff:
						mijl = mijl2
						break
					elif ls[mijl2] > ls[i]-minDiff:
						l = mijl2-1
					else:
						k = mijl2+1
				break
			elif ls[mijl] > ls[i]-minDiff:
				m = mijl-1
			else:
				n = mijl+1
		else:
			continue
		used.append(mijl)
		counter += 1
	return counter


v = [1, 2, 3, 4, 5, 6]
b = 4
print(maxPairs(v, b))


def taskOfPairing(freq):
	# Write your code here
	ls = []
	for i in range(len(freq)):
		ls.extend([i+1 for _ in range(freq[i])])
	i = 0
	counter = 0
	while i < len(ls)-1:
		if ls[i+1] - ls[i] <= 1:
			del ls[i:i+2]
			counter += 1
		else:
			i += 1
	return counter


v = [3, 5, 4, 3]
print(taskOfPairing(v))

