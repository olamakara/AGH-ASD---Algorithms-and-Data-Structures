# VIII egzamin zadanie B
# za pomoca floyda-warshalla tworzymy garf min sciezek i sumujemy z niego sciezki pomiedzy kolejnymi szarymi punktami


def robot(G, P):
    # lista sasiedztwa
    n = len(G)
    p = len(P)
    # Floyd-Warshall
    D = [[float('inf') for _ in range(n)] for _ in range(n)]
    for u in range(n):
        for v, wei in G[u]:
            if u < v:
                D[u][v] = D[v][u] = wei
    for k in range(n):
        for u in range(n):
            for v in range(n):
                D[u][v] = min(D[u][v], D[u][k] + D[k][v])
    # min sciezka przechodzaca przez punkty z P
    path_cost = 0
    for i in range(p - 1):
        path_cost += D[P[i]][P[i + 1]]
    return path_cost


