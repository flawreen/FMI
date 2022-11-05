"""
Se citește un cuvânt. Să se șteargă din cuvânt toate aparițiile primei litere. Se va afișa un mesaj de forma: După ștergerea literei 'X' șirul obținut este "S" de lungime L folosind diferite tipuri de formatare.
"""

s = input("dati sirul ")
c = s[0]
s = s.replace(c, "")  # !!!!s=
print(s)
print(f"După ștergerea literei '{c}', șirul obținut este \"{s}\" de lungime {len(s)}")
