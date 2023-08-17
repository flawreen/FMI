n = int(input())
ls = [x for x in input().split()]
indici = [-1 for _ in range(n)]
for i in range(n-1):
	if abs(ord(ls[i+1][-1]) - ord(ls[i][0])) == 1:
		
