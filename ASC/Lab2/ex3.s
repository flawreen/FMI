.data
    x: .long 19
    y: .long 15
    str1: .asciz "x > y"
    str2: .asciz "x <= y"

.text

.globl main

main:

    movl x, %eax
    cmp y, %eax
    jg afis1 # %eax {x} > y
    jmp afis2

afis1:
    movl $4, %eax
    movl $1, %ebx
    movl $str1, %ecx
    movl $6, %edx
    int $0x80
    jmp et_exit

afis2:
    movl $4, %eax
    movl $1, %ebx
    movl $str2, %ecx
    movl $6, %edx
    int $0x80

et_exit:
    movl $1, %eax
    movl $0, %ebx
    int $0x80
