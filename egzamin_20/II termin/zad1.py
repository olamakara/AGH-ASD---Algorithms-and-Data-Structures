# 19/20 egzamin termin 2 zadanie 1
# wersja zachlanna: wkladam do kolejki kolejne indeksy ktore moze odwiedzic zaba i wyciagam po min liczbie skokow
from egz_2_1_testy import runtests
from queue import PriorityQueue


# algorytm zachlanny
def zbigniew(A):
    n = len(A)
    q = PriorityQueue()
    place = 0
    min_jumps = 0
    # (jumps, dist, energy)
    q.put((0, 0, A[0]))
    while place != n - 1:
        jumps, dist, energy = q.get()
        ind = dist + 1
        while ind < n and ind <= dist + energy:
            q.put((jumps + 1, ind, energy - ind + dist + A[ind]))
            ind += 1
        min_jumps = jumps
        place = dist
    return min_jumps


runtests(zbigniew)
