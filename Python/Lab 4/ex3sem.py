"""
3. a) Scrieți o funcție care, dat numele unui fișier, determină și returnează frecvența
caracterelor din fișier
b) Se consideră fișierele caractere1.in si caractere2.in. Să se afișeze pentru fiecare fișier
frecvența caracterelor.
c) Să se afișeze caracterele comune celor două fișiere și frecvența cu care se repetă în
ambele fișiere (minimul frecvențelor cu care apar în cele două fișiere)
d) Să se modifice punctul c) pentru a afișa caracterele care apar în cel puțin unul dintre
fișiere, cu frecvența totală.
"""
# a)
def frecv(nume_fisier):
    fisier = open(nume_fisier)
    freq = {}
    for c in fisier.read():
        if 'a' <= c <= 'z':
            freq.setdefault(c, 0)
            freq[c] += 1
    return freq
# b)
freq1 = frecv('caractere.in')
freq2 = frecv('caractere2.in')
print(f"caractere.in:\n{freq1}\ncaractere2.in:\n{freq2}")

# c)
comune = {x: min(freq1[x], freq2[x]) for x in set(freq1).intersection(freq2)}
print(comune)

# d)
total = {x: freq1.get(x, 0) + freq2.get(x, 0) for x in set(freq1).union(freq2)}
print(total)
