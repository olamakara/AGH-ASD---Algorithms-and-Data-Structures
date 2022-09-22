# III egzamin zadanie B
# max mst
# co do wyjatku: trzeba zostawic pierwsza krawedz, ktora nie bedzie potrzebna do mst


def fix(G):
    g = []
    n = len(G)
    for u in range(n):
        for v, weight in G[u]:
            if u > v:
                g.append((weight, u, v))
    return g


def lufthansa(G):

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        x = find(x)
        y = find(y)
        if rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[x] = y
            if rank[x] == rank[y]:
                rank[y] += 1

    n = len(G)  # liczba wierzcholkow
    res = 0
    tmp = False
    G = fix(G)
    # (weight, u, v)
    G.sort(key=lambda x: x[0], reverse=True)
    parent = [i for i in range(n)]
    rank = [0 for _ in range(n)]
    for weight, u, v in G:
        if find(u) != find(v):
            union(u, v)
        elif tmp:
            res += weight
        else:
            tmp = True
    return res


G = [
    [(1, 15), (2, 5), (3, 10)],
    [(0, 15), (2, 8), (4, 5), (5, 12)],
    [(0, 5), (1, 8), (3, 5), (4, 6)],
    [(0, 10), (2, 5), (4, 2), (5, 11)],
    [(1, 5), (2, 6), (3, 2), (5, 2)],
    [(1, 12), (4, 2), (3, 11)]
]
print(lufthansa(G))

