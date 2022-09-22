# 21/22 egzamin termin 1 zadanie 1
# O(nlogn) - trzeba wybierac najwieksze dopoki dni sie nie skoncza


def snow(S):
    n = len(S)
    suma = 0
    S.sort(reverse=True)
    i = 0
    while S[i] - i > 0 and i < n:
        suma += S[i] - i
        i += 1
    return suma
