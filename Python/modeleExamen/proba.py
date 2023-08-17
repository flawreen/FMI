def decryptPassword(s):
	# Write your code here
	ls = []
	numbers = []
	l = len(s)
	i = 0
	while i < l:
		if s[i].isdigit() and s[i] != '0':
			numbers.append(s[i])
		elif i+2 < l and i+1 < l and s[i].isupper() and s[i+2] == '*':
			ls.append(s[i+1])
			ls.append(s[i])
			i += 1
		elif s[i] == '0':
			ls.append(numbers.pop())
		elif s[i].isalpha():
			ls.append(s[i])
		i += 1
	res = "".join([s for s in ls])
	return res


print(decryptPassword("pTo*Ta*O"))
