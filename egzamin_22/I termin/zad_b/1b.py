# 21/22 egzamine termin 1 zadanie 2
# tworze dodatkowa tablice do policzenia ile jest lisci na danym poziomie
# przechodzac rekurencyjnie w dol zliczam liscie i zaznaczam w self.x max level poddrzewa,
# a potem przechodze drugi raz i sumuje krawedzie, ktore trzeba odciac - dzieci wezlow z levelem na ktorym jest
# najwyzszy i najszerszy oraz te krawedzie przy wezlach, gdzie self.x jest mniejszy od tego levela


class Node:
    def __init__( self ):
        self.left = None # lewe poddrzewo
        self.right = None # prawe poddrzewo
        self.x = None # pole do wykorzystania przez studentów


def print_bst(root):
    if root is not None:
        print(root.x, '- ', end='')
        print_bst(root.right)
        print_bst(root.left)


def widentall(T):

    def go_in(root, level):
        nonlocal tab_levels
        if level >= len(tab_levels):
            tab_levels.append(1)
        else:
            tab_levels[level] += 1
        if root.right is None and root.left is None:
            root.x = level
            return
        if root.right is not None:
            go_in(root.right, level + 1)
            root.x = root.right.x
        if root.left is not None:
            go_in(root.left, level + 1)
            if root.x is not None:
                root.x = max(root.x, root.left.x)
            else:
                root.x = root.left.x

    def go_in_2(root, level):
        nonlocal max_i, default
        if root.x < max_i:
            default += 1
            return
        if root.right is not None:
            if level == max_i:
                default += 1
            else:
                go_in_2(root.right, level + 1)
        if root.left is not None:
            if level == max_i:
                default += 1
                return
            go_in_2(root.left, level + 1)

    level, max_, max_i, default = 0, 0, 0, 0
    tab_levels = []
    go_in(T, level)
    for i in range(len(tab_levels) - 1, -1, -1):
        if tab_levels[i] > max_:
            max_ = tab_levels[i]
            max_i = i
    go_in_2(T, level)
    return default


A = Node()
B = Node()
C = Node()
A.left = B
A.right = C
D = Node()
E = Node()
B.left = D
B.right = E
F = Node()
E.right = F
G = Node()
F.right = G
print(widentall(A))
