s = input()
s1 = sorted(s)
ls = []
c = s1[0]
j = 0
for i in range(1, len(s)):
	if s1[i] != c:
		ls.append((c, i-j))
		j = i
		c = s1[i]
ls.append((c, len(s)-j))
ls.sort(key=lambda x: (-x[1], x[0]))
print("\n".join([f"{ls[i][0]} {ls[i][1]}" for i in range(3)]))