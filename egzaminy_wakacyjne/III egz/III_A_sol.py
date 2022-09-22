# III egzamin zadanie A
# problem plecakowy na listach odsylaczowych
# trzeba zmienić self.x w testach


class Node:
    def __init__(self, wyborcy, koszt, fundusze):
        self.next = None
        self.wyborcy = wyborcy
        self.koszt = koszt
        self.fundusze = fundusze
        self.x = [0 for _ in range(fundusze + 1)]


# funkcja dla jednych wyborow
# problem plecakowy
# trzeba zapamietywac poprzedni plecak
def election(ele):
    # ele - wskaznik na lancuch okregow danych wyborow
    for i in range(ele.koszt, ele.fundusze + 1):
        ele.x[i] = ele.wyborcy
    prev = ele.x
    ele = ele.next
    guard = ele
    while ele is not None:  # okregi
        for j in range(ele.fundusze + 1):  # fundusze
            ele.x[j] = prev[j]
            if j - ele.koszt >= 0:
                ele.x[j] = max(ele.x[j], prev[j - ele.koszt] + ele.wyborcy)
        prev = ele.x
        guard = ele
        ele = ele.next
    return guard.x[guard.fundusze]


def wybory(T):
    n = len(T)
    cnt = 0
    for i in range(n):
        if T[i] is not None:
            cnt += election(T[i])
    return cnt


wyb1okr1 = Node(3, 8, 15)
wyb1okr2 = Node(2, 7, 15)
wyb1okr3 = Node(4, 5, 15)
wyb1okr1.next = wyb1okr2
wyb1okr2.next = wyb1okr3
wyb2okr1 = Node(4, 7, 8)
wyb2okr2 = Node(5, 2, 8)
wyb2okr1.next = wyb2okr2
wyb3okr1 = Node(3, 5, 10)
wyb3okr2 = Node(3, 5, 10)
wyb3okr1.next = wyb3okr2
T = [wyb1okr1, wyb2okr1, wyb3okr1]
print(wybory(T))
