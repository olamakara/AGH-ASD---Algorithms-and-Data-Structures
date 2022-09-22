#  20/21 kolokwium zaliczeniowe 2 zadanie 2
# tworzymy graf skierowany - krawedz tam gdzie moze przejsc z jednej liczby na druga
# sortujemy topologicznie, jesli pierwszy (najmniejszy) jest po ostatnim (najwiekszym) zwracam None
from kol_zal_2_2_testy import runtests


def topsort(G, s):

    def dfs_visit(u):
        nonlocal G, visited, res
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfs_visit(v)
        res.append(u)

    res = []
    n = len(G)
    visited = [False for _ in range(n)]
    visited[s] = True
    for u in G[s]:
        if not visited[u]:
            dfs_visit(u)
        visited[u] = True
    res.append(s)
    res.reverse()
    return res


def order(L, K):
    n = len(L)
    M = 10 ** K
    min_ = min(L)
    max_ = max(L)
    min_ind = 0
    for i in range(n):
        if L[i] == min_:
            min_ind = i
    H = [[] for _ in range(n)]
    for i in range(n):
        A = L[i] % M
        for j in range(n):
            B = L[j] // M
            if A == B:
                H[i].append(j)
    print(H)
    print(min_ind)
    R = topsort(H, min_ind)
    if L[R[0]] == min_ and L[R[-1]] == max_:
        for i in range(n):
            R[i] = L[R[i]]
        return R
    return None


runtests(order)
