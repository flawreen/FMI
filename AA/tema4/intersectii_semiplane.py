def ecuatie(a, b, c):
    global limite
    xmin, ymin, xmax, ymax = float("-inf"), float("-inf"), float("inf"), float("inf")
    if b == 0:
        if a < 0:
            limite[0][0] = c / -a
        else:
            limite[0][1] = -c / a
        xmin = max(xmin, limite[0][0])  # cel mai mare minim
        xmax = min(xmax, limite[0][1])  # cle mai mic maxim
    elif a == 0:
        if b < 0:
            limite[1][0] = c / -b
        else:
            limite[1][1] = -c / b
        ymin = max(ymin, limite[1][0])
        ymax = min(ymax, limite[1][1])
    if xmin > xmax or ymin > ymax:
        return False
    return True


def limite_finale():
    res = True
    for x in PP:
        res = res and ecuatie(x[0], x[1], x[2])
        # print(limite)
    return res


def isVoid():
    return limite[0][0] >= limite[0][1] or limite[1][0] >= limite[1][1]


def isInf():
    return limite[0][0] == float("-inf") or limite[1][0] == float("-inf") or limite[0][1] == float("inf") or limite[1][
        1] == float("inf")


def rez(void=True):
    if isVoid() or not void:
        print("VOID")
    elif isInf():
        print("UNBOUNDED")
    else:
        print("BOUNDED")


n = int(input())
PP = [[int(x) for x in input().split()] for _ in range(n)]
m = int(input())
limite = [[float("-inf"), float("inf")], [float("-inf"), float("inf")]]
rez(limite_finale())

