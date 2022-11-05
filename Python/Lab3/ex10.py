"""
Care atribuiri sunt incorecte + ce fac cele corecte pentru lista:
ls=list(range(7))
ls = [0, 1, 2, 3, 4, 5, 6]
ls[4:5]=45  -> TypeError
ls[4:5]="ab"  -> [0, 1, 2, 3, 'a', 'b', 5, 6]
ls[4:5]=ls[5:4]  -> SyntaxError
ls[4:5]=ls[3]  -> TypeError
ls[4:5]=ls[3:]  -> [0, 1, 2, 3, 3, 'a', 'b', 5, 6, 'b', 5, 6]
ls [4:5]=[ls[3]]  -> [0, 1, 2, 3, 3, 'a', 'b', 5, 6, 'b', 5, 6]
"""
ls = list(range(7))
print(ls)
ls[4:5] = ["ab"]
print(ls)
"""
Ce afișează următoarea secvență de cod?
ls=[0,0]
matr=[]
matr[:]=[ls]      matr -> [[0, 0]]
matr[1:]=[[1,1]]  matr -> [[0, 0], [1, 1]]
ls[0]=3           ls -> [3, 0], matr -> [[3, 0], [1, 1]]
print(matr)

[[3, 0], [1, 1]]
[0, [1, 1]]
"""
ls=[0,0]
matr=[]
matr[:]=[ls]
print(matr)
matr[1:]=[[1,1]]
ls[0]=3
print(matr)
