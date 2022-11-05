// 2. Fie s un string salvat in memorie si t un spatiu alocat cu aceeasi numar de octeti. Sa se obtina
// in t inversul string-ului s si sa se afiseze pe ecran.
.data
    s: .asciz "La multi ani"
    t: .space 13
.text

.globl main
main:
    
inversare:


afisare_string:
    movl $4, %eax
    movl $1, %ebx
    movl $t, %ecx
    movl $13, %edx
    int $0x80

etexit:
    movl $1, %eax
    xorl %ebx, %ebx
    int $0x80
