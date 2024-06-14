

def a():
    n, K = [int(x) for x in input().split()]
    s = [int(x) for x in input().split()]
    rez = [s[0]]
    suma_max = 0

    for i in range(1, len(s)):
        for x in rez:
            if x + s[i] <= K:
                rez.append(x + s[i])
                suma_max = max(suma_max, x + s[i])

    return suma_max


def b():
    n, K = [int(x) for x in input().split()]
    rez = 0
    for i in range(n):
        x = int(input())
        if rez + x <= K:
            rez += x
        else:  # Daca rez + x > K atunci rez devine x pentru a avea o sansa mai mare de a avea o suma maxina
            rez = max(rez, x)
    return rez
