def in_plan(a, b, c, x, y):
    return a * x + b * y + c <= 0


n = int(input())
PP = [[float(x) for x in input().split()] for _ in range(n)]
m = int(input())

for _ in range(m):
    x, y = [float(x) for x in input().split()]
    xmax, xmin, ymax, ymin = float("-inf"), float("inf"), float("inf"), float("-inf")
    for a, b, c in PP:
        if in_plan(a, b, c, x, y):
            if b == 0:
                xx = -c / a
                if a > 0:
                    if xx > x:
                        xmin = min(xmin, xx)
                else:
                    if xx < x:
                        xmax = max(xmax, xx)
            else:
                yy = -c / b
                if b > 0:
                    if yy > y:
                        ymax = min(ymax, yy)
                else:
                    if yy < y:
                        ymin = max(ymin, yy)

    if xmax == -float("inf") or xmin == float("inf") or ymax == float("inf") or ymin == -float("inf"):
        print("NO")
    else:
        print("YES")
        print(f"{((xmin - xmax) * (ymax - ymin)):.6f}")


