# 21/22 egzamin termin 2 zadanie 1
# O(n^2)
# algorytm tworzy listę n magazynow z pojemnoscia T
# pozniej przechodzi po wszystkich transportach oraz po wszystkich magazynach i dodaje transport do pierwszego magazynu,
# w ktorym sie zmiesci, zapamietujac przy tym ostatni uzyty magazyn,
# ktory zwraca jako odpowiedz


def coal( A, T ):
    n = len(A)
    magazyny = [T for _ in range(n)]
    ostatni_magazyn = 0
    for ladunek in A:
        for i in range(n):
            if magazyny[i] - ladunek >= 0:
                magazyny[i] -= ladunek
                ostatni_magazyn = i
                break
    return ostatni_magazyn
