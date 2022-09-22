# 21/22 egzamin termin 2 zadanie 2
# O(n)
# algorytm przechodzi po kazdej komnacie i w kazdej komnacie rozpatruje mozliwe przejscia do innych komnat
# jesli mozemy przejsc danymi drzwiami, tak zeby w skrzyni zostala odpowiednia ilosc zlota (nie zabierajac z niej przy
# tym wiecej niz 10, to max_dotarcia[w] = max(max_dotarcia[w], max_dotarcia[i] + min(g - k, 10))
# gdzie w to komnata do ktorej chcemy wejsc, i to komnata z ktorej przyszlismy, g to ilosc zlota w skrzyni,
# a k to ilosc zlota, ktore ma zostac w skrzyni


def magic( C ):
    n = len(C)
    max_dotarcia = [-1 for _ in range(n)]  # max ilosc zlota z jaka dotarlismy do i-tego wierzcholka
    max_dotarcia[0] = 0
    for i in range(n - 1):
        g = C[i][0]
        if max_dotarcia[i] != -1:
            for j in range(1, 4):
                k, w = C[i][j]
                if w != -1 and max_dotarcia[i] + g - k >= 0 and g - k <= 10:
                    max_dotarcia[w] = max(max_dotarcia[w], max_dotarcia[i] + min(g - k, 10))
    if max_dotarcia[n - 1] == -1:
        return -1
    return max_dotarcia[n - 1]
