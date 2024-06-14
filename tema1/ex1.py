import random
import math
import numpy as np


def fc(x):
    return a * x ** 2 + b * x + c


""" input
20
-1 2
-1 1 2
6
0.25
0.1
50

refac crossover, 2 puncte de rupere a si b interschimb ce e intre a si b
afisez cu |interschimbat|

"""


def incrucisare(populatie, first=False):
    participanti = []
    if first:
        g.write(f"\n\nProbabilitatea de incrucisare {p_recombinare}\n")

    # Generez un nr aleator si daca e mai mic decat p_recombinare atunci adaug indexul cromozomului in lista de participanti la incrucisare
    for i in range(dim):
        u = np.random.uniform()
        if first:
            g.write(f"{i + 1}: {populatie[i]} u={u}")

        if u < p_recombinare:
            if first:
                g.write(f"<{p_recombinare} participa\n")

            participanti.append(i)
        elif first:
            g.write("\n")

    # Fac incrucisarea 2 cate 2, daca am nr impar de participanti fac incrucisare intre ultimul si penultimul participant
    if len(participanti) < 2:
        if first:
            g.write("\nNu au fost selectati destui cromozomi pentru incrucisare!\n")
    else:
        for i in range(0, len(participanti) - 1, 2):
            # Aleg un punct de incrucisare aleator
            punct = random.randint(0, len(populatie[i]) - 1)
            punct2 = random.randint(0, len(populatie[i]) - 1)
            k, m = participanti[i], participanti[i + 1]
            if first:
                g.write(f"\nRecombinare dintre cromozomul {k + 1} cu cromozomul {m + 1}:\n")
                g.write(f"{populatie[k]}  {populatie[m]} punctele {punct} si {punct2}\n")
            p1, p2 = min(punct, punct2), max(punct, punct2)
            # populatie[k] = populatie[k][:punct] + populatie[m][punct:]
            # populatie[m] = populatie[m][:punct] + populatie[k][punct:]
            temp_k = populatie[k]
            populatie[k] = populatie[k][:p1] + populatie[m][p1:p2+1] + populatie[k][p2+1:]
            populatie[m] = populatie[m][:p1] + temp_k[p1:p2+1] + populatie[m][p2+1:]

            if first:
                g.write(f"Rezultat {populatie[k][:p1]}|{populatie[k][p1:p2+1]}|{populatie[k][p2+1:]}\t")
                g.write(f"{populatie[m][:p1]}|{populatie[m][p1:p2+1]}|{populatie[m][p2+1:]}\n")

        # Daca a fost selectat un numar impar de cromozomi pentru incrucisare, il combin pe penultimul cu ultimul
        if len(participanti) % 2 == 1:
            punct = random.randint(0, len(populatie[0]) - 1)
            k, m = participanti[-2], participanti[-1]
            if first:
                g.write(f"\nRecombinare dintre cromozomul {k + 1} cu cromozomul {m + 1}:\n")
                g.write(f"{populatie[k]}  {populatie[m]} punctele {punct} si {punct2}\n")
            p1, p2 = min(punct, punct2), max(punct, punct2)
            # populatie[k] = populatie[k][:punct] + populatie[m][punct:]
            # populatie[m] = populatie[m][:punct] + populatie[k][punct:]
            temp_k = populatie[k]
            populatie[k] = populatie[k][:p1] + populatie[m][p1:p2 + 1] + populatie[k][p2 + 1:]
            populatie[m] = populatie[m][:p1] + temp_k[p1:p2 + 1] + populatie[m][p2 + 1:]

            if first:
                g.write(f"Rezultat {populatie[k][:p1]}|{populatie[k][p1:p2 + 1]}|{populatie[k][p2 + 1:]}\t")
                g.write(f"{populatie[m][:p1]}|{populatie[m][p1:p2 + 1]}|{populatie[m][p2 + 1:]}\n")

    if first:
        g.write("\nDupa recombinare:\n")
        g.write("\n".join(
            f"{i + 1}: {populatie[i]} x= {decodificare(populatie[i])} f= {fc(decodificare(populatie[i]))}"
            for i in range(dim)))
        g.write("\n")

    return populatie


def codificare(x):
    len_cromozom = int(math.ceil(math.log2((dom[1] - dom[0]) * pow(10, precizie))))
    nr = int((x / (dom[1] - dom[0])) * (2 ** len_cromozom - 1) - dom[0])
    return bin(nr & ((1 << len_cromozom) - 1))[2:].zfill(len_cromozom)
    # fac o masca de {len_cromozomi} biti si scad 1 ca sa aiba toti bitii 1


def decodificare(bin_str):
    len_cromozom = int(math.ceil(math.log2((dom[1] - dom[0]) * pow(10, precizie))))
    x = int(bin_str, 2) / (2 ** len_cromozom - 1)
    return x * (dom[1] - dom[0]) + dom[0]


def mutatie(populatie, first=False):  # mutatie rara
    cromozomi_mutati = set()
    if first:
        g.write(f"\nProbabilitate de mutatie pentru fiecare gena {p_mutatie}\n")
    for i in range(dim):
        # generez o valoare aleatoare si daca e mai mica decat p_mutatie fac o mutatie pe o pozitie aleatoare din cromozomul i
        u = np.random.uniform()
        if u < p_mutatie:
            cromozomi_mutati.add(i)
            p = np.random.randint(0, len(populatie[i]))
            bit_schimbat = "0" if populatie[i][p] == "1" else "1"
            populatie[i] = f"{populatie[i][:p]}{bit_schimbat}{populatie[i][p + 1:]}"

    if first:
        g.write("Au fost modificati cromozomii:\n")
        for cromozom in cromozomi_mutati:
            g.write(f"{cromozom + 1}\n")
        g.write("\nDupa mutatie:\n")
        g.write("\n".join(
            f"{i + 1}: {populatie[i]} x= {decodificare(populatie[i])} f= {fc(decodificare(populatie[i]))}"
            for i in range(dim)))
        g.write("\n")

    return populatie


def selectie(populatie, first=False):  # selecte elitista
    global F
    fx = [fc(decodificare(cromozom)) for cromozom in populatie]
    F = sum(fx)
    p_selectie = [xi / F for xi in fx]
    fitness = [round(fc(decodificare(cromozom)), precizie) for cromozom in populatie]

    # Caut cromozomul elitist
    i_elitist, fit_elitist = 0, fitness[0]
    for i in range(len(fitness)):
        if fitness[i] > fit_elitist:
            i_elitist = i
            fit_elitist = fitness[i]

    # Cromozomul elitist ramane in urmatoarea generatie
    populatie_noua = [populatie[i_elitist]]

    # Vectorul cu capetele de intervale
    interv = [0]
    for i in range(len(p_selectie)):
        interv.append(interv[i - 1] + p_selectie[i])
    interv.append(1.0)

    if first:
        g.write("\nProbabilitati selectie:\n")
        g.write("\n".join(f"cromozom {i + 1} probabilitate {p_selectie[i]}" for i in range(dim)))
        g.write("\n")
        g.write("\n\nIntervale probabilitati selectie:\n")
        g.write(" ".join(f"{x}" for x in interv))
        g.write("\n")

    # generez un nr random intre 0 si 1 si folosesc cautare binara
    # sa vad in care interval apartine
    # apoi iau indexul capatului din dreapta al intervalului
    # si adaug cromozomul cu acel index la populatia noua
    for i in range(dim):
        x, st, dr, gasit = np.random.uniform(), 0, len(interv) - 1, -1
        while st <= dr:
            mij = (st + dr) // 2
            if interv[mij] <= x < interv[mij + 1]:
                gasit = mij
                break
            elif interv[mij] > x:
                dr = mij - 1
            else:
                st = mij + 1
        if gasit > dim:  # Daca indexul din interval este mai mare decat nr de cromozomi selectez ultimul cromozom
            gasit = len(populatie) - 1
        if first:
            g.write(f"\nu={x} selectam cromozomul {gasit}")
        populatie_noua.append(populatie[gasit - 1])

    if first:
        g.write("\n\nDupa selectie:\n")
        g.write("\n".join(
            f"{i + 1}: {populatie_noua[i]} x= {decodificare(populatie_noua[i])} f= {fc(decodificare(populatie_noua[i]))}"
            for i in range(dim)))

    return populatie_noua


with open("input.txt", "r") as f:
    dim = int(f.readline())
    dom = [int(x) for x in f.readline().split()]
    a, b, c = [int(x) for x in f.readline().split()]
    precizie = int(f.readline())
    p_recombinare = float(f.readline())
    p_mutatie = float(f.readline())
    nr_etape = int(f.readline())
populatie_initiala = [codificare(random.uniform(dom[0], dom[1])) for _ in range(dim)]
evolutie_maxim = []
F = 0

g = open("evolutie.txt", "w+")
g.write("Populatie initiala:\n")
g.write("\n".join(
    f"{i + 1}: {populatie_initiala[i]} x= {decodificare(populatie_initiala[i])} f= {fc(decodificare(populatie_initiala[i]))}"
    for i in range(dim)))
g.write("\n\n")

for i in range(nr_etape):
    global populatie_curenta
    if i == 0:
        populatie_curenta = selectie(populatie_initiala, first=True)
        populatie_curenta = incrucisare(populatie_curenta, first=True)
        populatie_curenta = mutatie(populatie_curenta, first=True)
    else:
        populatie_curenta = selectie(populatie_curenta)
        populatie_curenta = incrucisare(populatie_curenta)
        populatie_curenta = mutatie(populatie_curenta)

    evolutie_maxim.append((max(fc(decodificare(populatie_curenta[i])) for i in range(len(populatie_curenta))),
                           F / len(populatie_curenta)))

g.write("\n\nEvolutia maximului:\n")
g.write(f"{'Valoare maxima':<30}Fitness mediu\n")
g.write("\n".join(f"{x[0]:<30}{x[1]}" for x in evolutie_maxim))
