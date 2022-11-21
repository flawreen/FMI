"""
4. Se dă un fișier cu cuvinte pe mai multe linii separate prin spații. Scrieți un program care să
determine grupurile de cuvinte din fișier care au aceleași litere (nu neapărat cu aceeași
frecvență). Numele fișierului de intrare se va citi de la tastatură, iar grupurile formate din
cel puțin două cuvinte se vor scrie în fișierul text “litere.txt”, câte un grup pe o linie.
Cuvintele din fiecare grup vor fi sortate după lungime, iar în caz de lungimi egale,
lexicografic, iar grupurile se vor scrie în fișier în ordinea descrescătoare a numărului de
elemente din mulțimile literelor.
Pentru fișierul de intrare:
apar mare
si amara rapa para
par isi rama
fișierul de ieșire va fi
par apar para rapa
rama amara
si isi
"""
f = open("files/cuvinte.in")
# cheia dictionarului va fi multimea de litere dar facem frozenset (imutabil)
d = {}
for linie in f:
    for cuv in linie.split():
        litere = frozenset(cuv)
        exista = d.setdefault(litere, [cuv])
        if cuv not in d[litere]:
            d[litere].append(cuv)
f.close()
def cheie(x):
    return len(x), x
litere = list(d.keys())  # sortam cheile
litere.sort(key=len, reverse=True)
print(*litere, sep="\n")
g = open("files/litere.txt", "w")
for mult_litere in litere:
    if len(d[mult_litere]) > 1:
        d[mult_litere].sort(key=cheie)  # key=cheie e ca key=len
        g.write(" ".join(d[mult_litere]))
        g.write("\n")
