# egzamin II zadanie B
# tworzymy drzewo bst sufiksow (1 - left, 0 - right) i dodajemy z listy D 1 tam gdzie jest dany sufiks
# potem przechodzimy po otrzymanym drzewie i sumujemy log10 z mozliwosci wystepowania sufiksow z Q
from math import log10


class BST:
    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None
        self.val = 0


def kryptograf(D, Q):

    # wprowadzam wartosci z D
    # prawo - sufiks 0, lewo - sufiks 1
    def insert_D(root, string):
        if not len(string):
            return
        suff = string[-1]
        if suff == '1':  # 1
            if root.left is None:
                left = BST()
                root.left = left
                left.parent = root
            root.left.val += 1
            insert_D(root.left, string[:-1])
        else:  # 0
            if root.right is None:
                right = BST()
                root.right = right
                right.parent = root
            root.right.val += 1
            insert_D(root.right, string[:-1])

    def  get_sum(root, string):
        if not len(string):
            return log10(root.val)
        suff = string[-1]
        if suff == '1':  # 1
            return get_sum(root.left, string[:-1])
        else:  # 0
            return get_sum(root.right, string[:-1])

    d = len(D)
    q = len(Q)
    root = BST()
    root.val = d
    for i in range(d):
        insert_D(root, D[i])
    res = 0
    for i in range(q):
        res += get_sum(root, Q[i])
    return res


D = ["1100", "100", "0", "1111", "1101"]
Q = ["", "1", "11", "0", "1101"]
print(kryptograf(D, Q))


