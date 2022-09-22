# 19/20 egzamin termin 1 zadanie 3
# bucket sort, tylko przy wkladaniu do bucketow trzeba zamieniac liczby na log,
# zeby podzial jednostajny sie faktycznie przydal
from egz_1_3_testy import runtests
from math import log


def convert(number, a, diff):
    return int(log(number, a) / diff)


def insertion_sort(tab):
    # do sortowania bucketow w teoretycznym czasie stalym
    n = len(tab)
    for i in range(1, n):
        rem = tab[i]
        j = i - 1
        while j >= 0 and tab[j] > rem:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = rem
    return tab


def fast_sort(tab, a):
    # liczby rozlozone sa rownomiernie na przedziale [0,1]
    n = len(tab)
    res = []
    diff = 1 / n
    buckets = [[] for _ in range(n)]
    for i in range(n):
        ind = convert(tab[i], a, diff)
        buckets[ind].append(tab[i])
    for bucket in buckets:
        res += insertion_sort(bucket)
    return res


runtests(fast_sort)
