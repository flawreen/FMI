"""
1. Se dau n cuburi cu laturile diferite două câte două. Fiecare cub are o culoare, codificată cu
un număr de la 1 la p (p dat). Să se construiască un turn de înălţime maximă de cuburi în care
un cub nu poate fi aşezat pe un cub de aceeaşi culoare sau cu latură mai mică decât a sa
"""
with open("files/cuburi.in") as f:
    n, p = [int(x) for x in f.readline().split()]
    cuburi = []
    for linie in f:
        ls = linie.split()
        cuburi.append((int(ls[0]), int(ls[1])))
cuburi.sort(key=lambda x: x[0], reverse=True)
sol = [cuburi[0]]
inaltime = cuburi[0][0]
for cub in cuburi[1:]:
    if cub[1] != sol[-1][1]:
        sol.append(cub)
        inaltime += cub[0]
print(cuburi, sol, inaltime, sep="\n")