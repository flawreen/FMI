// Fie v: .long 15, 3, 27, 10, 19, 2, 8 un array de dimensiune n: .long 7, declarat in .data
// Sa se determine minimul din array, si sa se afiseze printr-un apel la printf: Minimul este %d
.data
    v: .long 15, 3, 27, 10, 19, 2, 8
    n: .long 7
    min: .space 4
    formatStr: .asciz "Minimul este %d"
.text
.globl main
main:
    mov $v, %edi
    mov $0, %ecx
    movl (%edi, %ecx, 4), %ebx
    movl %ebx, min

et_for:
    cmp n, %ecx
    je et_exit
    movl (%edi, %ecx, 4), %ebx
    cmp min, %ebx
    jl minim
    jmp continuare
minim:
    movl %ebx, min
continuare:
    incl %ecx
    jmp et_for

et_exit:
    movl $1, %eax
    xorl %ebx, %ebx
    int $0x80
