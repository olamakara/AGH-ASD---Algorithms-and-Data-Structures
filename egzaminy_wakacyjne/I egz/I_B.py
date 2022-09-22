# I egzamin zadanie B
# rozmnozenie wierzchokow - razy 4, musimy wykonac dokladnie 4 ruchy i czwartym musi byc lotnisko
# trzeba uwazac zeby przez dworzec ani lotnisko nie przeszlo dwa razy
from queue import PriorityQueue


# zamienia liste krawedzi na liste sasiedztwa
def fix(G):  # (u, v, p)
    max_ = (max(G, key=lambda x: x[1]))[1]  # jest opcja ze trzeba bedzie znalezc max z wszystkich wierzcholkow
    g = [[] for _ in range(max_ + 1)]
    for u, v, p in G:
        g[u].append([p, v])
        g[v].append([p, u])
    return g


def turysta(G, D, L):  #dijkstra
    # D - dworzec, L - lotnisko, G = (weight, vertex)

    def relax(v, u, step, weight):
        nonlocal dist, G
        if dist[v][step] > dist[u][step - 1] + weight:
            dist[v][step] = dist[u][step - 1] + weight
            return True
        return False

    G = fix(G)
    n = len(G)
    q = PriorityQueue()
    dist = [[float('inf') for _ in range(5)] for _ in range(n)]
    visited = [[False for _ in range(5)] for _ in range(n)]
    for i in range(1, 5):
        visited[D][i] = True
    for i in range(4):
        visited[L][i] = True
    dist[D][0] = 0
    q.put((0, D, 0))
    while not q.empty():
        d, u, s = q.get()
        if s < 4:
            for w, v in G[u]:
                if relax(v, u, s + 1, w) and not visited[v][s + 1]:
                    q.put((dist[v], v, s + 1))
    return dist[L][4]


G = [
(0, 1, 9), (0, 2, 1),
(1, 2, 2), (1, 3, 8),
(1, 4, 3), (2, 4, 7),
(2, 5, 9), (3, 4, 7),
(4, 5, 1), (3, 6, 8),
(4, 6, 1), (5, 6, 1),
(0, 6, 1)
]
D = 0
L = 6
print(turysta(G, D, L))
