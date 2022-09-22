# VII egzamin zadanie B
# O(n) - ponoc drzewo przedzialowe


# O(n^2)
# przechodze rownolegle dwoma petlami i zapisuje czy bralam juz dane drzewo (raz, wiecej albo w ogle)
# i na biezaco uaktualniam wynik
def ogrod(S, V):
    n = len(S)
    v = len(V)
    max_res = 0
    for i in range(n):
        trees = [0] * (v + 1)
        trees[S[i] - 1] = 1
        res = V[S[i] - 1]
        max_res = max(max_res, res)
        for j in range(i + 1, n):
            if trees[S[j] - 1] == 0:
                trees[S[j] - 1] = 1
                res += V[S[j] - 1]
            elif trees[S[j] - 1] == 1:
                trees[S[j] - 1] = 2
                res -= V[S[j] - 1]
            max_res = max(max_res, res)
    return max_res


S = [2, 3, 1, 1, 4, 1, 2, 4, 1]
V = [5, 3, 6, 6]
print(ogrod(S, V))
