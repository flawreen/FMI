"""
6. În fișierul text “date.in” sunt memorate, pe linii, numele și prenumele studenților dintr-o
grupă. Să se scrie un program care să genereze conturile de email ale studenților și
parolele temporare, după care să le salveze în fișierul text “date.out”. Contul de email al
unui student va fi de forma prenume.nume@s.unibuc.ro, iar parola temporară va fi de
forma o literă mare, 3 litere mici și 4 cifre. Se va scrie o funcție care generează parola
folosind funcții din modulul random https://docs.python.org/3/library/random.html
(randint, choice, choices pentru constantele string.ascii_uppercase, string.digits etc din
modulul string https://docs.python.org/3/library/string.html ). Exemplu de generare de 3
litere mici:
random.choices(string.ascii_letters , k=3)

date.in
Bobocea Andrei
Marinescu Ciprian
Vasile Dragos

date.out (exemplu,parolele sunt generate aleator)
andrei.bobocea@s.unibuc.ro,Wadf2133
ciprian.marinescu@s.unibuc.ro,Qsdd2111
dragos.vasile@s.unibuc.ro,Bbyt7690
"""
from random import choice, choices
from string import ascii_uppercase, ascii_lowercase, digits
def genAuth(date):
    auth = [[f"{nume[1]}.{nume[0]}@s.unibuc.ro"] for nume in date]
    for x in auth:
        passw = choice(ascii_uppercase) + "".join(choices(ascii_lowercase, k=3)) + "".join(choices(digits, k=4))
        x.append(passw)
    return auth
f = open("files/date.in", "r")
studenti = [line.rstrip("\n").lower().split() for line in f]
f.close()
conturi = genAuth(studenti)
g = open("files/date.out", "w")
g.write("\n".join([",".join([x for x in student]) for student in conturi]))
g.close()
