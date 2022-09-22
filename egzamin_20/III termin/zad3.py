# 19/20 egzamin termin 3 zadanie 3
# merge list odsylaczowych
from egz_3_3_testy import runtests


class Node:
    def __init__(self, val):
        self.next = None
        self.val = val


def merge(L1, L2):
    guard = Node(None)
    res = guard
    while L1 is not None and L2 is not None:
        if L1.val > L2.val:
            guard.next = L2
            L2 = L2.next
            guard = guard.next
        elif L1.val < L2.val:
            guard.next = L1
            L1 = L1.next
            guard= guard.next
        else:
            guard.next = L2
            L2 = L2.next
            guard = guard.next
            guard.next = L1
            L1 = L1.next
            guard = guard.next
    if L1 is not None:
        guard.next = L1
    else:
        guard.next = L2
    return res.next


def merge_sort(tab):
    n = len(tab)
    for i in range(n - 1):
        tab[i + 1] = merge(tab[i], tab[i + 1])
    return tab[n - 1]


runtests(merge_sort)
