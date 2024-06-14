class Node:
    def __init__(self, info, g=0, h=0, parent=None):
        self.info = info
        self.parent = parent
        self.g = g
        self.h = h
        self.f = self.g + self.h

    def drumRadacina(self):
        node = self
        path = []
        while node is not None:
            path.insert(0, node)
            node = node.parent
        return path

    def inDrum(self):
        node = self
        while node.parent is not None:
            if node.info == node.parent.info:
                return True
            node = node.parent
        return False

    def __repr__(self):
        return "{} g={} ({})".format(
            self.info, self.g, "->".join([str(x) for x in self.drumRadacina()])
        )

    def __str__(self):
        return str(self.info)

    def __eq__(self, elem):
        return (self.f, self.g) == (elem.f, elem.g)

    def __lt__(self, elem):
        return self.f < elem.f or (self.f == elem.f and self.h < elem.h)


class Graf:
    def __init__(self, matrix, start, scopes, h):
        self.matrix = matrix
        self.start = start
        self.scopuri = scopes
        self.h = h  # vector de estimatii

    def scop(self, info_nod):
        return info_nod in self.scopuri

    def estimeaza_h(self, infoNod):
        return self.h[infoNod]

    def succesori(self, node):
        list_successors = []
        for infoSuccesor in range(len(self.matrix[node.info])):
            if self.matrix[node.info][infoSuccesor] > 0 and not node.inDrum():
                list_successors.append(Node(
                    infoSuccesor,
                    node.g + self.matrix[node.info][infoSuccesor],
                    self.estimeaza_h(infoSuccesor),
                    node
                ))
        return list_successors


def aStarSolMultiple(graph, nsol):
    queue = [Node(graph.start)]

    while queue:
        current_node = queue.pop(0)
        if graph.scop(current_node.info):
            print(repr(current_node))
            nsol -= 1
            if nsol == 0:
                return
        list_successors = graph.succesori(current_node)
        queue += list_successors
        queue.sort()


m = [
    [0, 3, 5, 10, 0, 0, 100],
    [0, 0, 0, 4, 0, 0, 0],
    [0, 0, 0, 4, 9, 3, 0],
    [0, 3, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 4, 0, 5],
    [0, 0, 3, 0, 0, 0, 0],
]
start = 0
scopuri = [4, 6]
h = [0, 1, 6, 2, 0, 3, 0]

gr = Graf(m, start, scopuri, h)

aStarSolMultiple(gr, 5)
