# VI egzamin zadanie A
# musimy znalezc pierwsze nie-silne haslo

# O(nk + nlogn)
# 2x sortowanie, najpierw po ilosci liter, a pozniej po ilosci znakow i szukamy s-tego w tablicy

# O(nk)
# robimy jakby buckety po ilosci znakow
# i szukamy s-tej pozycji quickselectem
# (obliczamy ktora pozycje powinno miec haslo w buckecie i je znajdujemy po ilosci liter - quickselectem)


def counter(string):
    n = len(string)
    cnt = 0
    for i in range(n):
        if 96 < ord(string[i]) < 123:
            cnt += 1
    return cnt


def quickselect(A, p, k, r):
    # A - tablica, p - poczatek, r - koniec,
    # k - indeks, na ktorym znajduje sie szukamy element po posortowaniu

    def partition(p, r):
        x = counter(A[r])
        i = p - 1
        for j in range(p, r):
            if counter(A[j]) <= x:
                i += 1
                A[i], A[j] = A[j], A[i]
        A[i + 1], A[r] = A[r], A[i + 1]
        return i + 1

    if p == r:
        return A[p]
    if p < r:
        q = partition(p, r)
        if q == k:
            return A[q]
        elif q < k:
            return quickselect(A, q + 1, k, r)
        else:
            return quickselect(A, p, k, q - 1)


def google(H, s):
    n = len(H)
    if s > n:
        return ''
    max_length = 0
    for i in range(n):
        max_length = max(max_length, len(H[i]))
    buckets = [[] for _ in range(max_length + 1)]
    for i in range(n):
        buckets[len(H[i])].append(H[i])
    i = max_length
    while s > len(buckets[i]):
        s -= len(buckets[i])
        i -= 1
    arr = buckets[i]
    m = len(arr)
    tmp = quickselect(arr, 0, m - s, m - 1)
    return tmp


H = ['aba', 'abc', 'ab1', 'abab', 'a1a1', 'aa12a']
s = 3
A = [3, 3, 2, 4, 2, 3]
print(google(H, s))