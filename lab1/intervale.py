a, b = map(int, input().split())
m = int(input())
interv = []
for i in range(m):
    x, y = map(int, input().split())
    interv.append((x, y, i))

interv.sort(key=lambda f: f[0])

p = a
sol = [interv[0]]

while p < b:
    sel = interv[0]
    for t in interv:
        if t[0] > p:
            break
        if t[1] > sel[1]:
            sel = t
    if sel == (0, 0) or (len(sol) > 1 and sel == sol[-1]):
        print(0)
        exit(0)
    else:
        sol.append(sel)
        p = sel[1]

print(len(sol))
for t in sol:
    print(t[2] + 1, end=" ")
