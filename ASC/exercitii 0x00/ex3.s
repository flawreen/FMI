//1. Fie x, y doua numere natruale salvate in memorie. Sa se scrie un program care calculeaza in
//doua moduri (x/16) + (y × 16).
.data
    x: .long 33
    y: .long 1
    z: .long 16
    p: .asciz "PASS\n"
    f: .asciz "FAIL\n"
.text
.globl main
main:
    movl x, %eax
    movl y, %ebx
var1:
    movl $0, %edx
    movl x, %eax
    divl z
    movl %eax, %ebx
    movl y, %eax
    mull z
    add %eax, %ebx

var2:
    movl x, %eax
    sar $4, %eax
    movl %eax, %ecx
    movl y, %eax
    sal $4, %eax
    add %eax, %ecx

verificare:
    cmp %ebx, %ecx
    je pass
    jmp fail

pass:
    movl $4, %eax
    movl $1, %ebx
    movl $p, %ecx
    movl $6, %edx
    int $0x80
    jmp etexit

fail:
    movl $4, %eax
    movl $1, %ebx
    movl $f, %ecx
    movl $6, %edx
    int $0x80

etexit:
    movl $1, %eax
    xorl %ebx, %ebx
    int $0x80
