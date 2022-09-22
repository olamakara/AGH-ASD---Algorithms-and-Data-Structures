# 20/21 egzamin termin 3 zadanie 2
# drzewo binarne prefiksow 0/1
# najpierw wkladam wszystkie wyrazy do drzewa, a potem zczytuje liczby bardzo ladne
# bardzo ladny wyraz - jest prefiksem przynajmniej dwoch wyrazow ('1' to tez prefiks '1')
# oraz wyraz nie jest ladny kiedy po dolozeniu 0/1 jest ladny


class Node:
    def __init__(self):
        self.right = None
        self.left = None
        self.parent = None
        self.val = 0
        self.string = ''


def double_prefix(L):

    def insert(root, string):
        if not len(string):
            return
        if string[0] == '1':
            if root.right is None:
                right = Node()
                right.parent = root
                root.right = right
                root.right.string = root.string + '1'
            root.right.val += 1
            insert(root.right, string[1:])
        else:
            if root.left is None:
                left = Node()
                left.parent = root
                root.left = left
                root.left.string = root.string + '0'
            root.left.val += 1
            insert(root.left, string[1:])

    def read(root):
        if root.right is not None and root.left is not None:
            if root.val >= 2 > root.left.val and root.right.val < 2:
                res.append(root.string)
            read(root.right)
            read(root.left)
        elif root.right is not None:
            if root.val >= 2 > root.right.val:
                res.append(root.string)
            read(root.right)
        elif root.left is not None:
            if root.val >= 2 > root.left.val:
                res.append(root.string)
            read(root.left)

    l = len(L)
    root = Node()
    for i in range(l):
        insert(root, L[i])
    res = []
    read(root)
    return res


L = ['0100', '0110', '1010', '1']
print(double_prefix(L))
