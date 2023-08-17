"""
1. Se dă un vector a=(a1,...an) de tip munte (există un indice i astfel încât a1<a2<...< ai > ai+1>...>an;
ai se numește vârful muntelui). Propuneți un algoritm O(log n) care determină vârful muntelui (în
calculul complexității algoritmului nu se consideră și citirea vectorului). [1] exc 1,cap. 5
date.in
5
4 8 10 11 5
date.out
11
"""


def caut(v, ls, ld):
	if ls >= ld:
		return -1
	if ld - ls == 2:
		return max(v[ls], v[ld-1])
	m = (ls+ld) // 2
	if v[m-1] < v[m] > v[m+1]:
		return v[m]
	elif v[m-1] < v[m]:
		return caut(v, m+1, ld)
	else:
		return caut(v, ls, m-1)


v = [int(x) for x in input().split()]
n = len(v)
# ls = 0
# ld = n-1
# rez = -1
# while ls < ld:
# 	m = (ls+ld) // 2
# 	if v[m-1] < v[m] > v[m+1]:
# 		rez = m
# 		break
# 	elif v[m-1] < v[m]:
# 		ls = m+1
# 	else:
# 		ld = m-1
rez = -1
rez = caut(v, 0, n)

if rez == -1:
	print("Vectorul nu este de tip munte")
else:
	print(rez)
# O(log n)
