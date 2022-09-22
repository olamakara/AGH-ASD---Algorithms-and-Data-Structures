# VIII egzamin zadanie A


# O(n^2)
def reklamy(T, S, o):
    n = len(T)
    for i in range(n):
        T[i] = T[i][0], T[i][1], i
    T.sort(key=lambda x: x[0])
    max_gain = 0
    for i in range(n):
        if T[i][1] - T[i][0] <= o:
            max_gain = max(max_gain, S[T[i][2]])
        else:
            continue
        for j in range(i + 1, n):
            if T[i][1] < T[j][0]:
                if T[j][1] - T[i][0] <= o:
                    max_gain = max(max_gain, S[T[i][2]] + S[T[j][2]])
    return max_gain


T = [ (0, 3), (4, 5), (1, 4) ]
S = [ 5000, 3000, 15000 ]
o = 4
print(reklamy(T, S, o))

