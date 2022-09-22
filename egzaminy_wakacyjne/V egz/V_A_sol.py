# egzamin V zadanie A
# O(n^2) - po prostu idziemy kwadratowo po liscie i szukamy ciagu ktory da nam najwiecej
# O(n) - chyba drzewa przedzialowe - licznikowe


def inwestor(T):
    n = len(T)
    max_square = 0
    for i in range(n):
        prev = T[i]
        for j in range(i + 1, n):
            min_sum = min(prev, T[j])
            max_square = max(max_square, min_sum * (j - i + 1))
            prev = min_sum
    return max_square


T = [2, 1, 5, 6, 2, 3]
print(inwestor(T))
