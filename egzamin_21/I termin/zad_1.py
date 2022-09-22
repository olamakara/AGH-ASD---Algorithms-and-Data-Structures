# 20/21 egzamin termin 1 zadanie 1
# trzeba znalezc czynnik chaotycznosci listy, czyli
# o ile max miejsc trzeba przesunac liczby, zeby byly posortowane
# ten sam problem tylko z max chaotycznoscia (tu jest minimalna) ->
# -> trzeba tylko zrobic reverse() tablicy na poczatku

# zapamietujemy miejsca poczatkowe, sortujemy, i obliczamy max roznice w miejscach
# nie ma konkretnych informacji o liczbach, wiec uzywamy zwyklego sortowania
# O(nlogn)


from egz_1_1_testy import runtests


def partition(T, p, r):  # partition na przedziale T[p:r+1]
    x = T[r]
    i = p - 1
    for j in range(p, r):
        if T[j] <= x:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[r] = T[r], T[i + 1]
    return i + 1


def quick_sort(T, p, r):
    while p < r:
        q = partition(T, p, r)
        if q - p < r - q:
            quick_sort(T, p, q - 1)
            p = q + 1
        else:
            quick_sort(T, q + 1, r)
            r = q - 1


def chaos_index(T):
    n = len(T)
    for i in range(n):
        T[i] = (T[i], i)
    quick_sort(T, 0, n - 1)
    k = 0
    for i in range(n):
        k = max(k, abs(T[i][1] - i))
    return k


runtests(chaos_index)
