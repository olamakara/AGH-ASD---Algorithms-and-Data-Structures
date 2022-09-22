# IV egzamin zadanie B
# dla kazdeg wezla znalezc succ i pred i jesli sredna aryt = suc + pred to dodajemy do sumy ladnej
# zwracamy ladna sume


class Node:
    def __init__(self, key, parent):
        self.left = None
        self.right = None
        self.parent = parent
        self.key = key


def find(self, key):
    root = self
    while root is not None:
        if root.key == key:
            return root
        elif root.key < key:
            root = root.right
        else:
            root = root.left
    return None


def succ(self, key):  # zakladam ze nie ma min i max
    root = find(self, key)
    if root.right is not None:
        root = root.right
        while root.left is not None:
            root = root.left
        return root
    while root.parent is not None:
        prev = root
        root = root.parent
        if root.left == prev:
            return root
    return None


def pred(self, key):
    root = find(self, key)
    if root.left is not None:
        root = root.left
        while root.right is not None:
            root = root.right
        return root
    while root.parent is not None:
        prev = root
        root = root.parent
        if root.right == prev:
            return root
    return None


def sol(root, T):
    n = len(T)
    cnt = 0
    for i in range(n):
        suc = succ(root, T[i].key)
        pre = pred(root, T[i].key)
        average = (suc.key + pre.key) / 2
        if T[i].key == average:
            cnt += average
    return cnt


w11 = Node(11, None)
w5 = Node(5, w11)
w11.left = w5
w15 = Node(15, w11)
w11.right = w15
w3 = Node(3, w5)
w5.left = w3
w8 = Node(8, w5)
w5.right = w8
w12 = Node(12, w15)
w15.left = w12
w7 = Node(7, w8)
w8.left = w7
w10 = Node(10, w8)
w8.right = w10
T = [ w5, w7, w8, w11, w12 ]
print(sol(w11, T))
