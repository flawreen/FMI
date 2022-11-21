"""
5. Să se verifice dacă două șiruri de caractere formate doar din litere mici sunt anagrame sau
nu. Două șiruri sunt anagrame dacă sunt formate din aceleași litere, dar așezate în altă
ordine (sau, echivalent, unul dintre șiruri se poate obține din celălalt printr-o permutare a
caracterelor sale).

De exemplu, șirurile emerit și treime sunt anagrame, dar șirurile
emerit și treimi nu sunt!
"""
s1, s2 = {}, {}
for c in input():
    if c in s1:
        s1[c] += 1
    else:
        s1[c] = 1

for c in input():
    if c in s2:
        s2[c] += 1
    else:
        s2[c] = 1

if s1 == s2:
    print(f"Sunt anagrame!\n")
else:
    print(f"Nu sunt anagrame!\n")

