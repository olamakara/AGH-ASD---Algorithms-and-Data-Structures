# 20/21 egzamin termin 2 zadanie 1


def intuse(I, x, y):

    def dfs_visit(u):
        nonlocal I, n, visited, przydatnosc, y
        visited[u] = True
        if I[u][1] == y:
            przydatnosc[u] = True
            return
        for v in range(n):
            if I[u][1] == I[v][0]:
                if not visited[v] and I[v][1] <= y:
                    dfs_visit(v)
                if przydatnosc[v]:
                    przydatnosc[u] = True

    n = len(I)
    visited = [False for _ in range(n)]
    przydatnosc = [False for _ in range(n)]
    for u in range(n):
        if not visited[u] and I[u][0] == x:
            dfs_visit(u)

    res = []
    for i in range(n):
        if przydatnosc[i]:
            res.append(i)
    return res
