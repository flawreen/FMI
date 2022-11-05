//2. Fie s un spatiu alocat de 12 octeti. Folosind codul functiei read (vezi link-ul de mai sus unde
//sunt listate apelurile de sistem si codurile asociate) si stiind ca regula de incarcare este aceeasi
//ca in cazul functiei write, cititi in s de la tastatura (codul pentru stdin este 0) 12 caractere.
//Afisati-l pe s.
.data
    s: .space 12
.text
.globl main
main:
    movl $3, %eax
    movl $0, %ebx
    mov $s, %ecx
    movl 12, %edx
citire:
    int $0x80

    movl $4, %eax
    movl $1, %ebx
    movl $s, %ecx
    movl 12, %edx
afisare:
    int $0x80

etexit:
    movl $1, %eax
    xorl %ebx, %ebx
    int $0x80
