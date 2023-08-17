"""
5. Se dau doi vectori a și b de lungime n (ambii), cu elementele ordonate crescător. Propuneți un
algoritm cât mai eficient pentru a determina mediana vectorului obținut prin interclasarea celor doi
vectori O(log(n)) Mediana unui vector ordonat crescător cu număr impar de elemente este elementul
din mijloc, iar pentru un vector ordonat crescător cu număr par de elemente este media aritmetică a
celor două elemente din mijloc. Astfel, pentru vectorii
1 12 15 16 38
și
2 13 17 30 45
vectorul obținut prin interclasare este 1 2 12 13 15 16 17 30 38 45 și mediana lui va fi
(15+16)/2=15,5.
"""
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = []
n = len(a)
i, j = 0, 0
while i < n and j < n:
	if a[i] < b[j]:
		c.append(a[i])
		i += 1
	else:
		c.append(b[j])
		j += 1
while i < n:
	c.append(a[i])
	i += 1
while j < n:
	c.append(b[j])
	j += 1

print(c)
n = len(c)
if n//2 == 1:
	mediana = c[n//2]
else:
	mediana = (c[n//2-1] + c[n//2]) / 2
print(mediana)
