# 19/20 egzamin termin 3 zadanie 1
# trzeba policzyc srednice grafu
# czyli dwa bfs i trzeba zapisac odleglosci od jednego i drugiego wierzcholka,
# a potem znalezc na srednicy korzen, tak zeby byl min oddalony od obydwu wierzchokow
# jeden bfs z dowolnego liscia, a drugi z wierzcholka najbardziej oddalonego od tego liscia
from egz_3_1_testy import runtests
from queue import Queue


def bfs(G, s):
    n = len(G)
    q = Queue()
    dist = [0 for _ in range(n)]
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    visited[s] = True
    q.put(s)
    while not q.empty():
        u = q.get()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                dist[v] = dist[u] + 1
                q.put(v)
    return dist, parent


def best_root(L):
    n = len(L)
    leaf = 0
    # szukam liscia (musi byc, bo graf jest acykliczny)
    for i in range(n):
        if len(L[i]) == 1:
            leaf = i
            break
    from_leaf, parent = bfs(L, leaf)
    max_, ind = 0, 0
    # szukam najdalszego wierzcholka
    for i in range(n):
        if max_ < from_leaf[i]:
            max_ = from_leaf[i]
            ind = i
    print(leaf, ind)
    from_ind, par = bfs(L, ind)
    print(parent)
    # srednica
    d = from_ind[leaf]
    root = ind
    ind = parent[ind]
    diff = float('inf')
    while ind != leaf:
        tmp = abs(d - 2 * from_ind[ind])
        if tmp < diff:
            diff = tmp
            root = ind
        ind = parent[ind]
    return root


runtests(best_root)
