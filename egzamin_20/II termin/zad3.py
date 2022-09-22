# 19/20 egzamin termin 2 zadanie 3
# przeksztalcam liste taskow na graf skierowany i wykonuje sortowanie topologiczne,
# zeby znalezc poprawna sciezke przechodzaca przez wszystkie wierzcholki
# (zakladam, ze zawsze istnieje rozwiazanie)
from egz_2_3_testy import runtests


def top_sort(T):

    def dfs_visit(u):
        visited[u] = True
        for v in range(n):
            if T[u][v] and not visited[v]:
                dfs_visit(v)
        path.append(u)

    n = len(T)
    path = []
    visited = [False for _ in range(n)]
    for u in range(n):
        if not visited[u]:
            dfs_visit(u)
    return path


def tasks(T):
    n = len(T)
    # zamieniam na dag
    for i in range(n):
        for j in range(n):
            if not T[i][j] and i < j:
                T[i][j] = T[j][i] = 1
            elif T[i][j] == 1:
                T[j][i] = 0
            elif T[i][j] == 2:
                T[i][j] = 0
                T[j][i] = 1
    return top_sort(T)


runtests(tasks)
