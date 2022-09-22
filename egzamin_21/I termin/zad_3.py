# 20/21 egzamin termin I zadanie 3


from egz_1_3_testy import runtests


def przeciecie(p1, p2):
    if p1[0] < p2[0]:
        a1, b1 = p1
        a2, b2 = p2
    else:
        a2, b2 = p1
        a1, b1 = p2
    if b1 < a2:
        return None
    if b1 == a2:
        return b1, b1
    if b1 > a2 and b1 < b2:
        return a2, b1
    else:
        return a2, b2


# O(n^3)
# trzeba dla kazdej pary sprawdzic czy da sie znalezc k-2 przedzialow, ktore beda sie pokrywac z przecieciem tej pary
# trzeba pamietac o przypadku, gdy bez sensu jest dobieranie w pary!! czyli jak k=1
def kintersect(A, k):
    n = len(A)
    max_diff = -1
    max_tab = []
    if k == 1:
        for i in range(n):
            if A[i][1] - A[i][0] > max_diff:
                max_diff = A[i][1] - A[i][0]
                max_tab = [i]
        return max_tab
    for i in range(n):
        for j in range(i + 1, n):
            common = przeciecie(A[i], A[j])
            if common is not None:
                tmp = [i, j]
                a, b = common
                for m in range(n):
                    if m != i and m != j and A[m][0] <= a and A[m][1] >= b:
                        tmp.append(m)
                if len(tmp) == k and b - a > max_diff:
                    max_diff = b - a
                    max_tab = tmp
    return max_tab


runtests(kintersect)

