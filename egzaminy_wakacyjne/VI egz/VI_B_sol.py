# VI egzamin zadanie B
# dictionary.get(key, default=None) - for key key, returns value or default if key not in dictionary
# list(dictionary.values()) - return list of dictionary dict's values
# list(dictionary.keys())
# list(dictionary.items()) - list of (key,value)

# idziemy po ruchach w tablicy i jesli dane pole jest juz zaswiecone to gasimy,
# a jak nie ma danego pola to wrzucamy do slownika i zwracamy ilosc ostatecznie zapalonych zarowek (cos takiego)


def jump(M):
    curr = 0, 0
    dictionary = {(0, 0): True}
    jumps = {'LU': (-1, -2), 'UL': (-2, -1), 'UR': (-2, 1), 'RU': (-1, 2),
             'RD': (1, 2), 'DR': (2, 1), 'DL': (2, -1), 'LD': (1, -2)}
    for move in M:
        x, y = jumps[move]
        curr = curr[0] + x, curr[1] + y
        default = dictionary.get(curr, False)
        if default:
            dictionary[curr] = False
        else:
            dictionary[curr] = True
    n = len(dictionary)
    res = 0
    values = list(dictionary.values())
    for i in range(n):
        if values[i]:
            res += 1
    return res


M = ['UL', 'RD', 'LU', 'LU', 'RD', 'DL', 'UR', 'DR']
print(jump(M))
