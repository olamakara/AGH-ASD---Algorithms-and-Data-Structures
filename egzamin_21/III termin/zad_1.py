# 20/21 egzamin termin 3 zadanie 1
# ciag mr - ciag scisle rosnacy lub sciesle malejacy lub najpierw scisle malejacy, a potem rosnacy
# trzeba znalezc najdluzszy ciag mr
# sprawdzamy osobno dla samego lis i lds (scisle rosnacego/malejacego),
# a potem szukamy najbardziej korzystnego polaczenia lis i lds
from egz_3_1_testy import runtests


# O(n^2)
# zeby bylo O(nlogn) trzeba zrobic lis i lds w takiej wlasnie zlozonosci
def lis(A):
    n = len(A)
    maxi = 0
    F = [1 for _ in range(n)]
    P = [-1 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if A[i] < A[j] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1
                P[i] = j
        if F[i] > F[maxi]:
            maxi = i
    return maxi, F, P


def lds(A):
    n = len(A)
    maxi = 0
    F = [1 for _ in range(n)]
    P = [-1 for _ in range(n)]
    for i in range(1, n):
        for j in range(i):
            if A[i] < A[j] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1
                P[i] = j
        if F[i] > F[maxi]:
            maxi = i
    return maxi, F, P


def mr(I):
    n = len(I)
    max_lis, res_lis, path_lis = lis(I)
    max_lds, res_lds, path_lds = lds(I)
    max_both, max_val = 0, 0
    for i in range(n):
        for j in range(i + 1, n):
            if res_lds[i] + res_lis[j] > max_val and I[i] != I[j]:
                max_val = res_lds[i] + res_lis[j]
                max_both = i
                rem = j
    maximum = max(res_lis[max_lis], res_lds[max_lds], max_val)
    res = []
    if maximum == res_lis[max_lis]:
        while path_lis[max_lis] != -1:
            res.append(I[max_lis])
            max_lis = path_lis[max_lis]
        res.append(I[max_lis])
        print('lis')
    elif maximum == res_lds[max_lds]:
        while path_lds[max_lds] != -1:
            res.append(I[max_lds])
            max_lds = path_lds[max_lds]
        res.append(I[max_lds])
        res.reverse()
        print('lds')
    else:
        while path_lds[max_both] != -1:
            res.append(I[max_both])
            max_both = path_lds[max_both]
        res.append(I[max_both])
        res.reverse()
        max_both = rem
        while path_lis[max_both] != -1:
            res.append(I[max_both])
            max_both = path_lis[max_both]
        res.append(I[max_both])
        print('lds i lis')
    return res


runtests(mr)
