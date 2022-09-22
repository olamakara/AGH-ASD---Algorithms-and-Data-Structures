# 20/21 egzamin termin 2 zadanie 2


class Node:
    def __init__(self):
        self.edges = []
        self.weights = []
        self.ids = []
        self.worth = 0
        self.diff = []

    def addEdge(self, x, w, id):
        self.edges.append(x)
        self.weights.append(w)
        self.ids.append(id)


def worthy(T):
    if not T.edges:
        return
    n = len(T.edges)
    for i in range(n):
        worthy(T.edges[i])
        T.worth += T.weights[i]
        T.worth += T.edges[i].worth


def max_id(T, r_worth, id, weight):
    if not T.edges:
        return id
    n = len(T.edges)
    for i in range(n):
        T.diff.append(abs(r_worth - 2 * T.edges[i].worth - T.weights[i]))
        if T.diff[i] < weight:
            id = T.ids[i]
            weight = T.diff[i]
        id = max_id(T.edges[i], r_worth, id, weight)
    return id


def balance(T):
    worthy(T)
    return max_id(T, T.worth, 0, float('inf'))


A = Node()
B = Node()
C = Node()
D = Node()
E = Node()
A.addEdge(B, 6, 1)
A.addEdge(C, 10, 2)
B.addEdge(D, 5, 3)
B.addEdge(E, 4, 4)
print(balance(A))
