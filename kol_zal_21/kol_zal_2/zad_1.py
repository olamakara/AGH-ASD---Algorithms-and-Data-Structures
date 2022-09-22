# 20/21 kolokwium zaliczeniowe 2 zadanie 1
# jest zbiór prostokątów równoległych do osi x y i trzeba wskazac prostokat,
# po ktorego usunieciu pozostale beda mialy najwieksze pole przeciecia

# tworzymy dwie listy pomocnicze, jedna sumujaca wyrazy od 0 do i, druga od n - 1 do i
# za pomoca tych list mozemy okreslic pole po usunieciu jednego prostokata
# O(n)

from kol_zal_2_1_testy import runtests


def common_square(P1, P2):

    def find_common(a1, b1, a2, b2):
        if b1 < a2 or b2 < a1:
            return None
        elif a1 <= a2:
            if b1 <= b2:
                return a2, b1
            else:
                return a2, b2
        elif b1 <= b2:
            return a1, b1
        else:
            return a1, b2

    if P1 is None or P2 is None:
        return None
    x11, y11, x12, y12 = P1
    x21, y21, x22, y22 = P2
    resx = find_common(x11, x12, x21, x22)
    resy = find_common(y11, y12, y21, y22)
    if resx is not None and resy is not None:
        x1, x2 = resx
        y1, y2 = resy
        return x1, y1, x2, y2
    return None


def rect(D):
    # (x1, y1, x2, y2)
    n = len(D)
    L = [0 for _ in range(n)]
    R = [0 for _ in range(n)]
    tmp = [0 for _ in range(n)]
    L[0] = D[0]
    for i in range(1, n):
        L[i] = common_square(L[i - 1], D[i])
    R[n - 1] = D[n - 1]
    for i in range(n - 2, -1, -1):
        R[i] = common_square(R[i + 1], D[i])
    tmp[0] = R[1]
    tmp[n - 1] = L[n - 2]
    for i in range(1, n - 1):
        tmp[i] = common_square(L[i - 1], R[i + 1])
    res, ind = 0, 0
    for i in range(n):
        if tmp[i] is None:
            continue
        x1, y1, x2, y2 = tmp[i]
        P = abs((x2 - x1) * (y2 - y1))
        if P > res:
            res = P
            ind = i
    return ind


runtests(rect)
