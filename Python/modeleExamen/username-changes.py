def possibleChanges(usernames):
	rez = []
	for user in usernames:
		c = user[-1]
		ls = ['' for _ in range(len(user))]
		for i in range(len(user)-1, -1, -1):
			if user[i] < c:
				c = user[i]
				ls[i] = c
			else:
				ls[i] = c
		if "".join([s for s in ls]) == user:
			rez.append("NO")
		else:
			rez.append("YES")
	return rez


print(possibleChanges(["hydra"]))


