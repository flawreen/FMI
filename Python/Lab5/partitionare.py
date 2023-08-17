"""
Să presupunem că avem n activităţi (spectacole) care pentru a se desfășura au nevoie de o
resursă (sală de spectacole). Această resursă poate fi folosită de o singură activitate la un
moment dat. Fiecare activitate i are un timp de start si şi un timp de terminare ti, deci se poate
desfășura doar în intervalul [si, ti). Astfel, pe o resursă se pot planifica doar activități cu
intervalele de desfășurare disjuncte. Să se determine numărul minim k de resurse (săli de
spectacole) de care este nevoie pentru a efectua toate activitățile (spectacolele) și o planificare
a acestor activități pe cele k resurse.
Exemplu: pentru n=3 spectacole, care trebuie să se desfășoare în intervalele: [10, 14), [12, 16),
respectiv [17, 18), sunt necesare 2 săli, o programare optimă fiind:
o Sala 1: [10, 14) – spectacolul 1, [17, 18) – spectacolul 3
o Sala 2: [12, 16) – spectacolul 2
"""
def citire_intervale(fisier):
    """
    Structura listei ls:
    Tuplu:
        - numar spectacol
        - Lista:
            - ora inceput
            - ora sfarsit
    """
    with open(fisier) as f:
        i = 0
        ls = []
        for linie in f:
            i += 1
            linie = [int(x) for x in linie.strip("[)\n").split(", ")]
            ls.append((i, [linie[0], linie[1]]))
    return ls

def repartizare_sali(ls):
    """
    Structura listei sali:
    Lista:
        - numar sala
        - Lista:
            - Tuplu:
                - numarul spectacolului
                - Lista:
                    - ora inceput
                    - ora sfarsit
    """
    sali = []
    ls.sort(key=lambda x: x[1][1])
    i_sala = -1
    nr_spect = len(ls)
    while nr_spect > 0:
        t_ant_term = 0
        i_sala += 1
        sali.append([i_sala+1, []])
        i = 0
        while i < nr_spect:
            if ls[i][1][0] > t_ant_term:
                t_ant_term = ls[i][1][1]
                sali[i_sala][1].append(ls[i])
                ls.pop(i)
                nr_spect -= 1
            else:
                i += 1
    return sali

def afisare(ls):
    for sala in ls:
        print(f"Sala {sala[0]}:", end=" ")
        print(", ".join(f"[{spectacol[1][0]}, {spectacol[1][1]}) - spectacolul {spectacol[0]}" for spectacol in sala[1]))

ls = citire_intervale("files/partitionare.in")
ls = repartizare_sali(ls)
afisare(ls)
