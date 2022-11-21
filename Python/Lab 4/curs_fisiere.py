"""
suma dintr-un fisier
"""
with open("files/numere.in") as f, open("files/suma.out", "w") as g:
    for linie in f:
        s =  sum([int(x) for x in linie.split()])
        g.write(f"{s}\n")
