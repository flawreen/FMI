//1. Se dau doua numere naturale x si y. Sa se scrie un program in asamblare care sa realizeze
//interschimbarea lor. Sa se observe efectul folosind debugger-ul.
.data
    x: .long 4
    y: .long 32
.text

.globl main

main:
    movl x, %eax
    xorl y, %eax # x ^ y
    movl %eax, %ebx # ebx = x ^ y
    xorl y, %eax # x ^ y ^ y = x
    movl %eax, y # y = x^y^y = x

    xorl x, %ebx
    movl %ebx, x # x = x^y^x = y


etexit:
    movl $1, %eax
    xor %ebx, %ebx
    int $0x80
