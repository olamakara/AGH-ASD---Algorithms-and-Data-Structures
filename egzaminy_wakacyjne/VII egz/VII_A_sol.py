# VII egzamin zadanie A
from queue import Queue
from math import inf
# graf dwudzielny
# w zaleznosci od uzytych algorytmow i reprezentacji grafow jest rozna zlozonosc
# O(n^4) z edmondem i macierzowa reprezentacja
# O(n^2) - Ford-Fulkerson na liscie sasiedztwa


def bfs(graph, s, t, parent):
    queue = Queue()
    visited = [False] * len(graph)
    visited[s] = True
    queue.put(s)
    while not queue.empty():
        u = queue.get()
        for v in range(len(graph)):
            if not visited[v] and graph[u][v] != 0:
                visited[v] = True
                parent[v] = u
                queue.put(v)
    return visited[t]


def edmonds_karp_algorithm(graph, s, t):
    parent = [None] * len(graph)
    max_flow = 0
    while bfs(graph, s, t, parent):
        current_flow = inf
        current = t
        while current != s:
            current_flow = min(current_flow, graph[parent[current]][current])
            current = parent[current]
        max_flow += current_flow
        v = t
        while v != s:
            u = parent[v]
            graph[u][v] -= current_flow
            graph[v][u] += current_flow
            v = parent[v]
    return max_flow


def akademik(T):
    n = len(T)  # ilosc studentow
    max_ = 0
    cnt = 0
    for i in range(n):
        if T[i] == (None, None, None):
            cnt += 1
        for j in range(3):
            if T[i][j] is not None:
                max_ = max(max_, T[i][j])
    M = [[0 for _ in range(n + max_ + 3)] for _ in range(n + max_ + 3)]
    # max_ + 2 - ujscie, 0 - zrodlo, wszystkie elementy + 1
    for i in range(1, n + 1):
        M[0][i]  = 1
    for i in range(n + 1, n + max_ + 2):
        M[i][n + max_ + 2] = 1
    for i in range(n):
        st = i + 1
        for j in range(3):
            pok = T[i][j]
            if pok is not None:
                M[st][pok + n + 1] = 1
    print(T)
    return n - cnt - edmonds_karp_algorithm(M, 0, n + max_ + 2)


T = [(2, 3, None), (0, 1, 3), (0, 2, None), (1, 3, 4), (2, 3, None)]
print(akademik(T))
