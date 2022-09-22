# 20/21 kolokwium zaliczeniowe 1 zadanie 2
from kol_zal_1_2_testy import runtests


def dfs(G, no):
    # dfs na macierzy

    def dfs_visit(u):
        nonlocal n, no
        visited[u] = True
        for v in range(n):
            if G[u][v] and not visited[v] and v != no:
                dfs_visit(v)

    n = len(G)
    cnt = 0
    visited = [False for _ in range(n)]
    for u in range(n):
        if not visited[u] and u != no:
            cnt += 1
            dfs_visit(u)
    return cnt


def punkty_artykulacyjne(G):

    def help_me(u):
        nonlocal n, time
        children = 0
        dist[u] = time
        time += 1
        visited[u] = True
        low[u] = dist[u]
        tmp = False
        for v in range(n):
            if not visited[v]:
                if G[u][v]:
                    children += 1
                    parent[v] = u
                    help_me(v)
                    low[u] = min(low[u], low[v])
                    if low[v] >= dist[u] and parent[u] is not None:
                        tmp = True
            elif parent[u] != v and G[u][v]:
                low[u] = min(low[u], dist[v])
        if (parent[u] is None and children > 1) or tmp:
            # jesli jest korzeniem i ma 2 dzieci lub wiecej albo gdy spelnilo wczesniejszy warunek
            points.append(u)

    n = len(G)
    points = []
    dist = [0 for _ in range(n)]
    parent = [None for _ in range(n)]
    visited = [False for _ in range(n)]
    time = 0
    low = [float('inf') for _ in range(n)]
    for u in range(n):
        if not visited[u]:
            help_me(u)
    return points


def breaking(G):
    punkty = punkty_artykulacyjne(G)
    if not punkty:  # if empty
        return None
    max_, ind = 0, 0
    for i in punkty:
        cnt = dfs(G, i)
        if cnt > max_:
            max_ = cnt
            ind = i
    return ind


G = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 1, 1, 0]
]
H = [
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0]
]

runtests(breaking)
