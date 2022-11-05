"""
Se dă un vector v de n<100 numere naturale de cel mult două cifre. Să se determine
numărul de perechi disjuncte de elemente de egale (de forma (v[i], v[j]) cu i!=j și
v[i]=v[j]) care se pot forma cu elementele vectorului.
https://www.pbinfo.ro/probleme/2702/perechisosete

idee1: vector de frecventa
idee2: sortam vectorul
"""
v = [int(x) for x in input().split()]
frecv = [0 for i in range(100)]
for x in v:
    frecv[x] += 1

nr_perechi = 0
for f in frecv:
    if f != 0:
        nr_perechi += f // 2
print(nr_perechi)
