# Examinare seria 14

## A. layout, tranziții, media query (1.5 puncte)
1. Scrieți un fișier HTML `layout.html` care să conțină un div cu clasa `container`. În interiorul lui, adăugați încă alte 7 divuri. Creați un fișier `layout.css` în care să adăugați reguli CSS astfel încât pagina să arate ca în imaginea de mai jos și:
- fiecare coloană să aibă lățimea de 100px
- spațiul dintre linii și coloane să fie de 5px
- divurile să aibă padding de 25px
- textul să fie aliniat la dreapta
- divurile 1, 2, 3, 4, 5 vor avea border portocaliu, punctat, de 4px
- divurile :) vor avea border portocaliu, liniar, de 3px.

<img alt="layout" src="resources/images/layout.png" width="500px">

2. Adăugați reguli CSS astfel încât la trecerea mouse-ului deasupra divurilor ce conțin :)
- divurile vor avea border alb și fundal portocaliu
- se vor roti 90 de grade în sensul acelor de ceasornic, treptat, într-o tranziție de 0.3s.
 
<img alt="layout hover" src="resources/images/layout-hover.png" width="500px">

3. Scrieți un media query pentru ferestre cu lățimea între 200px și 600px astfel încât divurile să nu mai fie afișate cu layoutul de mai sus, ci în formatul default, unele sub altele, ocupând întreaga lațime a containerului, precum în imaginea de mai jos.

<img alt="layout" src="resources/images/layout-media.png" width="200px">

## B. fade to black: events, DOM, sessionStorage (2.5 puncte)

4. Scrieți un fișier HTML `fade.html` care să conțină un body gol și să încarce fișierul de stil `fade.css` pe care îl puteți găsi în directorul `resources`. Adăugați cod JavaScript în fișierul `fade.js` astfel încât la apăsarea butonului de mouse să se creeze un div nou în pagină. Fiecare div nou creat va conține o bulină de culoare `rgb(255,255,255)`. Poziția divului în pagină va fi aleatoare. Dimensiunea bulinei va fi și ea aleatoare, cu valoarea minimă posibilă 30px și cea maximă 150px.

5. Salvați în `sessionStorage` numărul de buline de pe ecran și afișați-l în colțul din dreapta sus a ecranului.

6. La apăsarea unei buline de pe ecran, aceasta va fi selectată. Bulina va avea border solid, roșu, de 3px. La apăsarea butonului de mouse în afara oricărei buline, atunci:
- dacă exista o bulină selectată, aceasta va fi deselectată (nu va mai avea border)
- dacă nu exista nicio bulină selectată, atunci se va crea o bulină nouă (ca mai sus, la exercițiul 4).

7. Bulinele se dizolvă. La fiecare 500 milisecunde se va apela o funcție `fade()` care va face toate bulinele de pe ecran să se întunece, prin schimbarea culorii: fiecare din cele trei componente de culoare RGB vor descrește la 0.9 din valoarea anterioară. Atunci când toate cele trei componente au valoarea 0, bulina (divul) va fi ștearsă din arborele DOM, iar numărul de buline salvat în `sessionStorage` va fi actualizat corespunzător.

8. Salvați bulinele! Pentru o bulină selectată, la apăsarea uneia din tastele r, g, b, valoarea componentei de culoare corespunzătoare pentru acea bulină va crește: i se va dubla valoarea. Dacă nicio bulină nu este selectată atunci când se apasă una din aceste taste, evenimentul nu va produce nicio schimbare.

## C. fun with flags: events, forms, fetch (2 puncte)

9. Scrieți un fișier HTML `flag.html` care să conțină un body gol. Adăugați cod JavaScript în fișierul `flag.js` astfel încât să afișați codificarea unui cuvânt introdus de utilizator în INTERCO (International Code of Signals), sistemul internațional de semnalizare maritim cu steaguri. Codificarea fiecărei litere (majusculă) este salvată în fișierul `flag.json` (care poate fi descărcat din directorul `resources`). Folosiți fetch și promisiuni pentru a accesa conținutul fișierului pe un server http local (porniți un server http folosind, de exemplu, Python). 

10. Utilizatorul introduce cuvântul de codificat într-un câmp text (element input) adăugat dinamic, folosind cod JavaScript. La scrierea unei majuscule (literă între A-Z), se va adăuga (dinamic, folosind cod JavaScript) imaginea steagului corespunzător literei introduse (salvată în câmpul `image` al obiectelor json din fișierul `flag.json`). Se vor afișa maxim 5 steaguri. Introducerea de către utilizator a altor caractere decât a literelor majuscule nu are niciun efect.

11. La trecerea cu mouse-ul deasupra unui steag, se va afișa sub imagini un text de forma `pronunție-nato - câmp-text` ce conține pronunția nato a literei corespunzătoare steagului și mesajul de semnalizat, din câmpul `text` al obiectelor json, precum în imaginea de mai jos.

<img alt="flags" src="resources/images/flags.png" width="500px">




