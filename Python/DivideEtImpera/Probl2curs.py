"""
Din lab
A = {a1, a2, ..., an} inclusa in N
M din N
Sa se det o subm a lui A de suma M (daca exista)

Indicatie:
+	Luam sau nu luam an pt a obtine suma M
Luam -> pb se reduce la a det o subm de suma M - an cu elem {a1, ..., an-1}
Nu il luam -> pb se reduce la a det o subm de suma M cu elem {a1, ..., a-1}

s[i][m] = se poate sau nu obtine suma m folosind {a1, ..., ai}
s[i][m] = s[i-1][m] sau (ai <= m si s[i-1][m-ai])
"""