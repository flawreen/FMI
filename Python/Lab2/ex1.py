# ex 13
# s = input("sirul codificat: ")
# s2 = []  # fac o lista in loc de str ""
# k = 0
# for i in range(len(s)):
#     if s[i].isdigit():
#         k = k * 10 + int(s[i])
#         continue
#     s2.extend(s[i] * k)  # daca pun s2 += s[i] * k se creeaza un nou str de fiecare data
#     k = 0
# s2 = "".join(s2)  # asa il fac sir de caractere din lista
# print(f'sirul decodificat: {s2}')

s = input("sirul decodificat:")
s2 = []
c = 1
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        c += 1
        if i == len(s)-1:
            # c += 1
            s2.append(str(c))
            s2.append(s[len(s) - 1])
            continue
        continue

    s2.append(str(c))
    s2.append(s[i-1])
    c = 1

if s[len(s) - 1] != s[len(s) - 2]:
    s2.append(str(1))
    s2.append(s[len(s)-1])
s2 = "".join(s2)
print(f'sirul codificat: {s2}')
