import copy

class NodArbore:
    def __init__(self, informatie, g=0, h=0, parinte=None):
        self.informatie = informatie
        self.parinte = parinte
        self.g = g
        self.h = h
        self.f = g + h

    def __eq__(self, elem):
        return (self.f, self.g) == (elem.f, elem.g)

    def __lt__(self, elem):
        return self.f < elem.f or (self.f == elem.f and self.h < elem.h)

    def drumRadacina(self):
        nod = self
        l = [nod]
        while nod.parinte:
            nod = nod.parinte
            l.insert(0, nod)
        return l

    def inDrum(self, infoNod):
        nod = self
        if infoNod == nod.informatie:
            return True
        while nod.parinte:
            nod = nod.parinte
            if infoNod == nod.informatie:
                return True

        return False

    def __str__(self):
        return str(self.informatie)

    # "c (a->b->c)"
    def __repr__(self):
        return f"{self.informatie} cost:{self.g} ({'->'.join(map(str, self.drumRadacina()))})"


class Graf:
    def __init__(self, start, scopuri):

        self.start = start
        self.scopuri = scopuri

    def scop(self, informatieNod):
        return informatieNod in self.scopuri

    def estimeaza_h(self, infoNod, euristica="banala"):
        if self.scop(infoNod):
            return 0
        if euristica == "banala":
            return 1
        if euristica == "euristica mutari":
            minH = float("inf")
            for scop in self.scopuri:
                h = 0
                for iStiva, stiva in enumerate(scop):
                    for iBloc, bloc in enumerate(stiva):
                        try:
                            if infoNod[iStiva][iBloc] != bloc:
                                h += 1
                        except:
                            h += 1
                if h < minH:
                    minH = h
            return minH
        if euristica == "euristica neadmisibila":
            return 1000  # un nr foarte mare
        if euristica == "euristica costuri":
            minH = float("inf")
            for scop in self.scopuri:
                h = 0
                for iStiva, stiva in enumerate(scop):
                    for iBloc, bloc in enumerate(stiva):
                        try:
                            if infoNod[iStiva][iBloc] != bloc:
                                h += ord(bloc) - ord('a') + 1  # singura dif fata de euristica mutari
                        except:
                            h += ord(bloc) - ord('a') + 1
                if h < minH:
                    minH = h
            return minH

    # (numar_misionari_mal_initial, numar_canibali_mal_initial, mal_curent)
    # mal initial = 1; mal final =0
    # mal curent= mal cu barca
    def succesori(self, nod, euristica):
        lSuccesori = []
        for i, stiva in enumerate(nod.informatie):
            if not stiva:
                continue
            copieStive = copy.deepcopy(nod.informatie)
            bloc = copieStive[i].pop()
            for j in range(len(copieStive)):
                if i == j:
                    continue

                infoSuccesor = copy.deepcopy(copieStive)
                infoSuccesor[j].append(bloc)
                if not nod.inDrum(infoSuccesor):
                    lSuccesori.append(NodArbore(
                        infoSuccesor,
                        nod.g + ord(bloc) - ord('a') + 1,
                        self.estimeaza_h(infoSuccesor, euristica),
                        nod))

        return lSuccesori


def breadthFirst(gr, nsol=2):
    coada = [NodArbore(gr.start)]
    while coada:
        nodCurent = coada.pop(0)
        if gr.scop(nodCurent.informatie):
            print(repr(nodCurent))
            nsol -= 1
            if nsol == 0:
                return
        coada += gr.succesori(nodCurent)


def aStarSolMultiple(gr, nsol=3):
    coada = [NodArbore(gr.start)]
    while coada:
        nodCurent = coada.pop(0)
        if gr.scop(nodCurent.informatie):
            print(repr(nodCurent))
            nsol -= 1
            if nsol == 0:
                return
        coada += gr.succesori(nodCurent)
        coada.sort()


def aStarSimplu(gr, euristica):
    OPEN = [NodArbore(gr.start)]
    CLOSED = []
    while OPEN:
        nodCurent = OPEN.pop(0)
        CLOSED.append(nodCurent)
        if gr.scop(nodCurent.informatie):
            print(repr(nodCurent))
            return

        lsuccesori = gr.succesori(nodCurent, euristica)
        for s in lsuccesori:
            gasitOpen = False

            for nodOpen in OPEN:
                if nodOpen.informatie == s.informatie:
                    gasitOpen = True
                    if nodOpen.f > s.f:
                        OPEN.remove(nodOpen)
                    else:
                        lsuccesori.remove(s)
                    break

            if not gasitOpen:
                for nodClosed in CLOSED:
                    if nodClosed.informatie == s.informatie:
                        if nodClosed.f > s.f:
                            CLOSED.remove(nodClosed)
                        else:
                            lsuccesori.remove(s)
                        break

        OPEN += gr.succesori(nodCurent)
        OPEN.sort()


# pentru a star simplu
# gr = Graf(start, scopuri)
# aStarSimplu(gr)
# """
# (0, 0, 0) cost:11 ((3, 3, 1)->(3, 1, 0)->(3, 2, 1)->(3, 0, 0)->(3, 1, 1)
# ->(1, 1, 0)->(2, 2, 1)->(0, 2, 0)->(0, 3, 1)->(0, 1, 0)->(0, 2, 1)->(0, 0, 0))
# """


# Punctul 1. b) este
# optional si 4
def obtineStive(sirStive):
    return [sirStiva.strip().split() if sirStiva != '#' else [] for sirStiva in sirStive.strip().split("\n")]


f = open("blocuri.txt", "r")
[sirStareStart, sirStariScop] = f.read().strip().split("=========")

start = obtineStive(sirStareStart)
scopuri = [obtineStive(sirScop) for sirScop in sirStariScop.split("---")]

gr = Graf(start, scopuri)
aStarSimplu(gr, "euristica mutari")





