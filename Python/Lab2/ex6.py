"""
a) Se citește un text și un număr natural k. Să se afișeze textul cifrat cu cifrul lui Cezar,
prin care fiecare literă (!doar literele) este înlocuită cu litera aflată peste 𝑘 poziții
la dreapta în alfabet în mod circular (valoarea 𝑘 reprezintă cheia secretă comună
pe care trebuie să o cunoască atât expeditorul, cât și destinatarul mesajului
criptat). De exemplu, pentru textul "O zi frumoasa!" și k=9 se va afișa “X ir
oadvxjbj! "

text = input("text decriptat: ")
k = int(input("k= "))
rez = []
k = k % 26
for s in text:
    if s.isupper():
        s = ord(s)
        # dif = 90 - s
        if k > (90 - s):
            # i = k - dif
            rez.append(str(chr(64 + k - (90 - s))))
        else:
            rez.append(str(chr(s + k)))
    elif s.islower():
        s = ord(s)
        # dif = 122 - s
        if k > (122 - s):
            # i = k - dif
            rez.append(str(chr(96 + k - (122 - s))))
        else:
            rez.append(str(chr(s + k)))
    else:
        rez.append(s)

rez = "".join(rez)
print(rez)"""

"""
b) Se citește un număr natural k și text criptat cu cifrul lui Cezar cu cheia k. Să se
afișeze textul decriptat.
"""
text = input("text criptat: ")
k = int(input("k= "))
rez = []
k = k % 26
for s in text:
    if s.isupper():
        s = ord(s)
        # dif = 90 - s  # diferenta de la ultima litera din alfabet la litera curenta
        if k > (90 - s):
            # i = k + dif  # cate pozitii se avanseaza de la inceputul alfabetului
            rez.append(str(chr(64 + k + (90 - s))))
        else:
            rez.append(str(chr(s - k)))
    elif s.islower():
        s = ord(s)
        # dif = 122 - s
        if k > (122 - s):
            # i = k + dif
            rez.append(str(chr(96 + k + (122 - s))))
        else:
            rez.append(str(chr(s - k)))
    else:
        rez.append(s)

rez = "".join(rez)
print(rez)
