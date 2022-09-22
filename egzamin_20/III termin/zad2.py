# 19/20 egzamin termin 3 zadanie 2
from egz_3_2_testy import runtests


# O(n^2)
# zapisujemy indeksy i sortujemy po koncach malejaco
# przechodzimy jedna petla do przodu, a druga w tyl i jesli sie zawiera to dodajemy
def tower(A):
    n = len(A)
    for i in range(n):
        A[i] = A[i][0], A[i][1], i
    A.sort(key=lambda x: x[1], reverse=True)
    T = [1 for _ in range(n)]
    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            if A[j][0] <= A[i][0] and A[j][2] < A[i][2]:
                T[i] = max(T[i], T[j] + 1)
    return max(T)


runtests(tower)
