# 20/21 egzamin termin 3 zadanie 3
from egz_3_3_testy import runtests


class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None
        self.key = None


# bez rekurencji
# przechodze iteracyjnie po drzewie w poszukiwaniu danego indeksu
# ide dopoki wysokosc nie jest 1, jesli lisc jest w prawej polowie, to ide root.right i zmieniam from_left liscia
# jesli lisc jest w lewej polowie to idziemy do root.left i zostawiamy from_left
# from_left to numer liscia liczac od lewej tego ktorego szukamy
def print_bst(root):
    if root is not None:
        print(root.key, '- ', end='')
        print_bst(root.right)
        print_bst(root.left)


def wys(ind):
    cnt = 1
    while ind != 1:
        ind = ind // 2
        cnt += 1
    return cnt


def maxin(T, X):
    max_ = float('-inf')
    for x in X:
        root = T
        h = wys(x)
        num_leafs = 2 ** (h - 1)
        from_left = x - num_leafs + 1
        while h != 1:
            if from_left <= num_leafs / 2:
                root = root.left
            else:
                root = root.right
                from_left = from_left - num_leafs / 2
            h -= 1
            num_leafs /= 2
        max_ = max(max_, root.key)
    return max_


runtests(maxin)
