# 19/20 egzamin termin 1 zadanie 1
# dijsktra z rozmnazaniem wierzcholkow na 3 (w zaleznosci od tego w jaki sposob dotrzemy na dana wyspe)
from egz_1_1_testy import runtests
from queue import PriorityQueue
from math import inf


def mean(trans):
    if trans == 8:
        return 0
    if trans == 5:
        return 1
    if trans == 1:
        return 2
    return -1


def islands(G, A, B):
    # macierz sasiedztwa
    # (dist, transport, vertex)
    # 0 - samolot, 1 - prom, 2 - most

    def relax(u, v, cost, last_u, last_v):
        if dist[v][last_v] > dist[u][last_u] + cost:
            dist[v][last_v] = dist[u][last_u] + cost
            return True
        return False

    n = len(G)
    q = PriorityQueue()
    dist = [[inf for _ in range(3)] for _ in range(n)]
    dist[A][0], dist[A][1], dist[A][2] = 0, 0, 0
    q.put((0, 0, A))
    q.put((0, 1, A))
    q.put((0, 2, A))
    while not q.empty():
        d, tr, u = q.get()
        for v in range(n):
            w = mean(G[u][v])
            if G[u][v] and w != tr and relax(u, v, G[u][v], tr, w):
                q.put((dist[v][w], w, v))
    return min(dist[B])


runtests(islands)
