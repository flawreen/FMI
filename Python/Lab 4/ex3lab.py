from math import sqrt
"""
3. a) Scrieți o funcție care primește ca parametru două nume de fișiere (variantă: un număr
variabil de nume de fișiere) și returnează un dicționar cu cuvintele care apar în cel puțin
unul dintre fișiere și frecvența totală cu care apare fiecare cuvânt (suma frecvențelor cu care
apar în fișiere). Cuvintele pot fi pe mai multe linii și pe o linie sunt separate prin spații.

dicționarul va fi {'a': 4, 'fost': 4, 'odata': 1, 'ca': 4, 'in': 6, 'povesti': 4, 'o': 1, 'data': 2,
'altadata': 1, 'basme': 2, 'alta': 1, 'nu': 1}
"""
def cuvinte(*fisier):
    cuvinte = {}
    for nume in fisier:
        f = open(nume)
        for linie in f:
            for cuv in linie.split():
                cuvinte.setdefault(cuv, 0)
                cuvinte[cuv] += 1
    return cuvinte
"""
b) Se consideră fișierele cuvinte1.in si cuvinte2.in. Să se afișeze cuvintele care apar în cel
puțin unul dintre fișiere ordonate crescător lexicografic

a alta altadata basme ca data fost in nu o odata povesti
"""
d = cuvinte("files/cuvinte1.in", "files/cuvinte2.in")
cuv = list(d.keys())
cuv.sort()
for i in cuv:
    print(i, end=" ")
print()
"""
c) Se consideră fișierul cuvinte1.in. Să se creeze o listă de perechi (cuvinte, frecvențe) cu
cuvintele care apar în fișier și frecvența cu care apar, ordonată descrescător după frecvență
(folosind funcția de la a)).

[('in', 3), ('povesti', 3), ('a', 2), ('fost', 2), ('ca', 2), ('odata', 1), ('o', 1), ('data', 1)]
"""
c1 = cuvinte("files/cuvinte1.in")
aparitii = list(c1.items())
aparitii.sort(key=lambda x: x[1], reverse=True)
print(aparitii)
"""
d) Să se determine un cuvânt care apare cel mai des în cuvinte2.in, folosind funcția de la a)
și funcția max. Dacă sunt mai multe posibilități, se va afișa cuvântul cel mai mic din punct
de vedere lexicografic

in
"""
c2 = cuvinte("files/cuvinte2.in")
ap = list(c2.items())
ap.sort()
ap.sort(key=lambda x: x[1], reverse=True)
print(ap[0][0])
"""
e) Pentru două documente text, 𝐹1 și 𝐹2, și {𝑐1, 𝑐2, ... , 𝑐𝑛 } mulțimea cuvintelor care apar
în cel puțin unul din cele două documente. Pentru 1 ≤ 𝑖 ≤ 𝑛, fie 𝑣𝑖1, 𝑣𝑖2 numărul de apariții
al cuvântului 𝑖 în primul, respectiv în al doilea document. Distanța cosinus dintre cele două
documente, notată 𝑑𝑐𝑜𝑠(𝐹1, 𝐹2 ), dintre 𝐹1 și 𝐹2 se calculează după formula:
                            suma(vi1*vi2)                   a
dcos(f1, f2) = --------------------------------------- = -------
                sqrt(suma(vi1)^2) * sqrt(suma(vi2)^2)     b * c
                
Să se calculeze distanța cosinus dintre fișierele caractere1.in si caractere2.in (folosind
funcția de la a) apelată separat pentru fiecare fișier) cu două zecimale.

0.79
"""
# folosesc dictionarul d de la pct a) - (cuvinte1.in, cuvinte2.in)
mult_cuv = set(d.keys())
# folosesc dictionarele c1 si c2 de la pct c) - cuvinte1.in, resp. d) - cuvinte2.in
a = sum([c1.get(x, 0) * c2.get(x, 0) for x in mult_cuv])
b = sqrt(sum([c1.get(x, 0)**2 for x in mult_cuv]))
c = sqrt(sum([c2.get(x, 0)**2 for x in mult_cuv]))
dcos = a / (b*c)
print(f"{dcos:.2f}")






