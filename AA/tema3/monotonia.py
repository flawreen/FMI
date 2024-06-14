n = int(input())
puncte = [[int(x) for x in input().split()] for _ in range(n)]
ls1, ls2 = [], []

minim = min(puncte)
i_min = puncte.index(minim)
maxim = max(puncte, key=lambda x: x[1])
i_max = puncte.index(maxim)

ls1 = puncte[i_min:] + puncte[:i_min]
ls2 = puncte[i_max:] + puncte[:i_max]

nr_ls1, nr_ls2 = 0, 0

for i in range(len(ls1) - 2):
    if ls1[i][0] < ls1[i + 1][0] and ls1[i + 1][0] > ls1[i + 2][0]:
        nr_ls1 += 1

if nr_ls1 == 1:
    print("YES")
else:
    print("NO")

for i in range(len(ls2) - 2):
    if ls2[i][1] > ls2[i + 1][1] and ls2[i + 1][1] < ls2[i + 2][1]:
        nr_ls2 += 1

if nr_ls2 == 1:
    print("YES")
else:
    print("NO")
