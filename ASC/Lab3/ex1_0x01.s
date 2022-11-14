# 1. (a) Sa se defineasca procedura perfect(x), cu x numar natural. Un numar este perfect daca
# este egal cu suma divizorilor sai pana la jumatate. Exemplu: 6 = 1 + 2 + 3; 28 = 1 + 2
# + 4 + 7 + 14;
# (b) Se dau de la tastatura un intreg n si un vector cu n elemente. Sa se afiseze pe ecran
# numarul de elemente perfecte.
.data
    x: .space 4
    n: .space 4
    v: .space 400
    jum: .space 4
    sum: .long 1
    nr_perfecte: .long 0
    afisare: .asciz "Numere perfecte in vector: %d.\n"
    citire: .asciz "%d"
.text
perfect: # (parametru x)
    push %ebp
    movl %esp, %ebp

    movl 8(%ebp), %ebx

    movl %ebx, %eax
    movl $2, %ecx
    movl $0, %edx
    divl %ecx

    movl %eax, jum  # limita loop-ului
    movl $2, %ecx  # pornesc de la 2 ca posibil divizor
    movl $1, sum  # initializez suma cu 1

    # fac suma divizorilor
    divizori: 
        cmp jum, %ecx
        jg verific_suma

        movl %ebx, %eax  # eax = x
        movl $0, %edx
        divl %ecx  # fac x / ecx
        
        cmp $0, %edx # verific daca ecx nu e divizor
        jne continuare

        # daca e divizor fac suma
        movl %ecx, %eax
        addl sum, %eax
        movl %eax, sum
        
        continuare:
        incl %ecx
        jmp divizori

    verific_suma:
    cmp sum, %ebx
    jne imperfect

    incl nr_perfecte

    imperfect:
    popl %ebp
    ret

.globl main
main:
    pushl $n
    pushl %citire
    call scanf
    popl %edx
    popl %edx

    movl $0, %ecx
    mov $v, %edi

    citire_vector:
        cmp n, %ecx
        je citit

        pushl $x
        pushl $citire
        call scanf
        popl %edx
        popl %edx

        movl x, (%edi, %ecx, 4)

        incl %ecx
        jmp citire_vector

    citit:
    pushl x
    call perfect
    popl %edx

et_exit:
    movl $1, %eax
    movl $0, %ebx
    int $0x80
