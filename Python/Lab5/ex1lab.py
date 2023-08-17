"""
1.a)Scrieți o funcție care să citească de la tastatură o listă cu elemente numere întregi. Numărul de elemente ale listei și elementele sale se vor citi în cadrul funcției
"""
def citire():
    global n
    n = int(input())
    ls = [int(x) for x in input().split()]
    return n, ls
"""
b)Scrieți o funcție care primește ca parametru o secvență s, un element x și, opțional, doi indici i și j și returnează poziția primului  element  mai  mare  decât x din s[i:j] (dacă i sau j  nu  se specifică, atunci comportamentul va fi cel de la feliere) și -1 în caz că nu există un astfel de element.
"""
def elem(s, x, i = 0, j = None):
    if j == None:
        j = n
    sol = -1
    for i in range(i, j):
        if s[i] > x:
            sol = i
            return sol
    return sol
"""
c) Scrieți un program care, folosind apeluri utile ale funcției definite anterior, afișează mesajul "Da"  în  cazul  în  care  o  listă  de  numere  întregi,  citită  de  la  tastatură,  este  sortată  strict descrescător sau mesajul "Nu" în caz contrar. Aceeași cerință și pentru o listă de cuvinte.
"""
n, ls = citire()
if elem(ls, ls[0]) != -1:
    print("Nu")
else:
    ok = 1
    for i in range(1, n):
        if elem(ls, ls[i], i-1) > i:
            ok = 0
            break
    if ok:
        print("Da")
    else:
        print("Nu")
