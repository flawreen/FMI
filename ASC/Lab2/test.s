.data
    x: .long 256
.text

.globl main

main:
    movl x, %eax
    mull x
    movl %eax, x

    mull x
    addl $10, %eax
    movl $2, %ebx
    mull %ebx


et_exit:
    movl $1, %eax
    xorl %ebx, %ebx
    int $0x80

