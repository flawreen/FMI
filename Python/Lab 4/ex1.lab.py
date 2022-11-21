"""
1. Scrieți un program care să determine grupurile de cuvinte dintr-un fișier text care p-rimează
între ele = au aceleași ultime p-litere (p citit de la tastatura). Numele fișierului de intrare se
va citi de la tastatură, iar grupurile se vor scrie în fișierul text “rime.txt”, câte un grup pe o
linie, în ordine descrescătoare în raport cu numărul de elemente din grup. Cuvintele din
fiecare grup vor fi sortate lexicografic descrescător.
De exemplu, pentru p=2 și fișierul:
ana dana
mere pere prune
bune
banana si gutui amare are
rime.txt va fi:
pere mere are amare
dana banana ana
prune bune
si
gutui
"""
nume_fisier = input("nume fisier: ")
f = open(nume_fisier)
p = int(input("p = "))
d = {}  # cheie = sufix
for linie in f:
    ls_cuvinte = linie.split()
    for cuv in ls_cuvinte:
        sufix_cuv = cuv[-p:]
        if sufix_cuv in d:  # cauta in cheile dictionarului
            d[sufix_cuv].append(cuv)
        else:
            d[sufix_cuv] = [cuv]
f.close()
print(d)
grupuri = list(d.values())  # punem list pe el ca sa facem .sort (altfel mergea .sorted)
grupuri.sort(key=len, reverse=True)  # în ordine descrescătoare în raport cu numărul de elemente din grup

g = open("files/rime.out", "w")
for grup in grupuri:
    grup.sort(reverse=True)  # Cuvintele din fiecare grup vor fi sortate lexicografic descrescător
    g.write(" ".join(grup))
    g.write("\n")
g.close()
