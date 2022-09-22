# V egzamin zadanie B
# trzeba znalezc pukty artykulacyjne, czyli takie ktoree rozspojniaja graf
# low(v) = min(d(v), min d(u), min low(w)), gdzie krawedz u-v jest krawedzia wsteczna
# a w-v to dziecko v


def dfs(G, s):
    # lista sasiedztwa

    def dfs_visit(u):
        nonlocal time
        children = 0
        visited[u] = True
        dist[u] = time
        time += 1
        low[u] = dist[u]
        for v in G[u]:
            if not visited[v]:
                children += 1
                parent[v] = u
                dfs_visit(v)
                low[u] = min(low[u], low[v])
                if low[v] >= dist[u] and parent[u] is not None:
                    art[u] = True
            elif parent[u] != v:
                low[u] = min(low[u], dist[v])
        if parent[u] is None and children >= 2:
            art[u] = True

    n = len(G)
    art = [False] * n
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    dist = [0 for _ in range(n)]
    low = [float('inf') for _ in range(n)]
    time = 0
    dfs_visit(s)  # nie trzeba w petli, bo mamy dane drzewo
    return art.count(True)


def koleje(B):
    m = len(B)
    n = 0
    for i in range(m):
        if B[i][0] > B[i][1]:
            B[i] = (B[i][1], B[i][0])
        n = max(n, B[i][1])
    n += 1
    B = sorted(B)
    G = [[] for _ in range(n)]
    G[B[0][0]].append(B[0][1])
    G[B[0][1]].append(B[0][0])
    for i in range(1, m):
        if B[i] != B[i-1]:
            G[B[i][0]].append(B[i][1])
            G[B[i][1]].append(B[i][0])
    return dfs(G, 0)


G = [[1, 3], [0, 2, 3], [1, 4], [0, 1], [2]]
B = [
(3, 1), (0, 1), (4, 2),
(1, 2), (0, 1), (2, 4),
(2, 4), (0, 3), (2, 4),
(1, 0), (2, 1)
]
print(koleje(B))

