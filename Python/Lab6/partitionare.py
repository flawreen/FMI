"""
ideea 2 - corecta
Cons. intervalul crescator dupa terminare si le distribuim pe rand in sali
- daca interv curent nu se poate programa intr-o sala deja folosita, cream o sala noua
- altfel -> il programam in sala cu timpul de terminare cel mai mare dintre cele compatibile (pt a lasa mai putin spatiu liber)
1, 2    1, 5    6, 8    4, 11
s1:[1, 2], [6, 8]
s2:[1, 5], [4, 11]

ideea 3
problema la ideea 2 este complexitatea de pe ramura altfel, dureaza ceva sa alegem sala cu cel mai mare timp de terminare compatibil
solutie => consideram intervalele cresc dupa inceput (cronologic) -> si le distribuim pe sali. In acest caz, cand avem de ales intre mai multe sali pt a programa intervalele nu conteaza sala pe care o alegem
1, 2    1, 5    6, 8    4, 11
s1:[1, 2], [4, 11]
s2:[1, 5], [6, 8]

corectitudine: 1) Daca avem k intervale care au un punct comun, avem nevoie de minim k sali.
               2) Ar. ca atunci cand algoritmul creeaza o sala noua k, exista k intervale care au un punct comun
Fie I = [s, t] intervalul pt care s-a creat sala k ==> (alg Greedy) Exista un interval Ij in sala j cu care I se intersecteaza pentru oricare j = 1,..,k-1. Deoarece intervalele sunt considerate cresc dupa inceput => s apartine Ij pentru oricare j = 1,...,k-1 deci exista k intervale: I1, I2,...,Ik-1, I care au un punct comun (pe s).

Facem un heap de perechi (tp_terminare, indice sala)
"""
import heapq
f=open("files/partitionare.in")
ls_intervale=[]
for linie in f:
    interv=[int(x) for x in linie.split()]
    ls_intervale.append(interv)
f.close()
ls_intervale.sort()
print(ls_intervale)
sali=[] # sali[i]= lista intervalelor programate in sala i
h = []  # heap de perechi (tp_terminare, indice sala)

for interval in ls_intervale:
    print(h)
    # cautam o sala la care putem adauga interval:
    # extragem din heap sala cu timpul de terminare cel mai mic
    if len(h) == 0:  # primul interval - heap gol, nu am nimic programat
        sala_noua = [interval]
        sali.append(sala_noua)  # prima sala
        heapq.heappush(h, (interval[1], 0))
    else:
        tp_terminare, i_sala = heapq.heappop(h)  # sala cu timpul de terminare cel mai mic
        # verificam daca interval se poate programa in aceasta sala
        if tp_terminare < interval[0]:
            sali[i_sala].append(interval)  # il adaugam in sala
            # inseram sala in heap cu noul timp de terminare
            heapq.heappush(h, (interval[1], i_sala))
        else:  # nu - cream o sala noua pentru interval
            sala_noua = [interval]
            sali.append(sala_noua)
            heapq.heappush(h, (interval[1], len(sali)-1))  # ultima sala, cea nou introdusa
            # punem inapoi in heap sala extrasa, pt ca nu am adaugat interval la ea
            heapq.heappush(h, (tp_terminare, i_sala))
i=1
for s in sali:
    print(f"sala {i}: ",end="")
    print(*s)  # print(s[0],s[1],....)
    i+=1
