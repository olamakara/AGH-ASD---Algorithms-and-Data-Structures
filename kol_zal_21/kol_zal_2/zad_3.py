#  20/21 kolokwium zaliczeniowe 2 zadanie 3
# trzeba znalezc liczbe krawedzi lezacych na jakiejs najkrotszej sciezce
# dwa ray dijkstra z s do t i z t do s, a potem spr czy dana krawedz nalezy do najkrotszej sciezki
from kol_zal_2_3_testy import runtests
from queue import PriorityQueue


def dijkstra(G, s):
    def relax(u, v, weight):
        nonlocal dist
        if dist[v] > dist[u] + weight:
            dist[v] = dist[u] + weight
            return True
        return False

    n = len(G)
    q = PriorityQueue()
    dist = [float('inf') for _ in range(n)]
    visited = [False for _ in range(n)]  # ?
    dist[s] = 0
    visited[s] = True
    q.put((0, s))
    while not q.empty():
        d_u, u = q.get()
        for v, d_v in G[u]:
            if relax(u, v, d_v) and not visited[v]:
                q.put((dist[v], v))
        visited[u] = True
    return dist


def paths(G, s, t):
    n = len(G)
    fromS = dijkstra(G, s)
    fromT = dijkstra(G, t)
    shortest = fromS[t]

    # PRZYPADEK GDY GRAF JEST NIESPOJNY
    if shortest == float('inf'):
        return 0

    cnt = 0
    for u in range(n):
        for v in range(len(G[u])):
            vertex, edge = G[u][v]
            if u < vertex:
                if (fromS[u] + fromT[vertex] + edge == shortest or
                        fromS[vertex] + fromT[u] + edge == shortest):
                    cnt += 1
    return cnt


runtests( paths )
