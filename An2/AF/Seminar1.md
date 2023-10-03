Examen -> 4p
Seminar (2 teme) -> 1p (latex)
Laborator ( 3 teme + colocviu) - 5p | 30% * (Teme) + 70% * (Test lab)

Tena 1 Lab -  6 probleme Deadline: Lab 3

G = (V, E)
d(x) = | N(x) |
N(x) = {y | (x, y) exista in G}
Nu se poate construi un graf cu un numar impar de noduri cu grad impar.
Complexitate DFS/BFS: matrice O(n^2), lista O(n+m)

BFS
1: 2
2: 3, 4, 5
3: 1, 5, 4
4: 6
5: 4
6: 
Incepem din 1
Coada: 1, 2, 3, 4, 5, 6
Rezultat BFS: 1, 2, 3, 4, 5, 6 (se adauga la solutie nodurile scoase din coada)
Rezultatul bfs poate alcatui un arbore:
1: 2
2: 3, 4, 5
4: 6
Care reprezinta drumuri minime
Si putem alcatui un vector de distante numerotat de la 1 la 6
[0, 1, 2, 2, 2, 3]


BFS E2
1: 2
2: 3, 5
3: 1, 5
4: 2, 3
5: 4
6:
Coada: 1, 2, 3, 5, 4, 6
BFS: 1, 2, 3, 5, 4, 6
[0, 1, 2, 2, 3, 4]



DFS
1: 2
2: 3, 5
3: 1, 5
4: 2, 3
5: 4
6:
1, 2, 5, 4, 6, 3


