# IV egzamin zadanie A
# longest non decreasing subsequence
# klasycznie w O(n^2), ale mozna tez w O(nlogn) - algorytm wytlumaczony na geekforgeeks


def mosty(T):
    n = len(T)
    max_ind = 0
    T.sort(key=lambda x: x[1])
    T.sort(key=lambda x: x[0])
    F = [1 for _ in range(n)]
    P = [-1 for _ in range(n)]
    for i in range(1, n):
        for j in range(i):
            if T[i][1] > T[j][1] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1
                P[i] = j
        if F[i] > F[max_ind]:
            max_ind = i
    return F[max_ind]


T = [(1, 2), (2, 3), (3, 0)]
print(mosty(T))
