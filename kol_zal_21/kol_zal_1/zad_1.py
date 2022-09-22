# 20/21 kolokwium zaliczeniowe 1 zadanie 1
# trzeba przekonwertowac drzewo bst na kopiec (najpierw do tablicy, a potem z powrotem wrzucic wartosci do bst
from kol_zal_1_1_testy import runtests


class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None
        self.value = None


def right(i):
    return 2 * i + 2


def left(i):
    return 2 * i + 1


def ConvertTree(T):

    def to_heap(T):
        if T.left is not None:
            to_heap(T.left)
        heap.append(T.value)
        if T.right is not None:
            to_heap(T.right)

    def transform(root, i):
        nonlocal n
        l = left(i)
        r = right(i)
        if l >= n:
            root.left = None
            root.right = None
            return
        if root.left is not None:
            root.left.value = heap[l]
        else:
            new = Node()
            new.parent = root
            root.left = new
            new.value = heap[l]
        transform(root.left, l)
        if r < n:
            if root.right is not None:
                root.right.value = heap[r]
            else:
                new = Node()
                new.parent = root
                root.right = new
                new.value = heap[r]
            transform(root.right, r)
        else:
            root.right = None

    heap = []
    to_heap(T)
    n = len(heap)
    T.value = heap[0]
    transform(T, 0)
    return T


runtests(ConvertTree)
