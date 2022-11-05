.data
    str1: .asciz "Sir 1\n"
    str2: .asciz "Sir 2\n"

.text

.globl main
main:

    jmp afis2
afis1:
    movl $4, %eax
    movl $1, %ebx
    movl $str1, %ecx
    movl $7, %edx
    int $0x80 # syscall
    jmp et_exit

afis2:
    movl $4, %eax
    movl $1, %ebx
    movl $str2, %ecx
    movl $7, %edx
    int $0x80 # syscall
    jmp afis1

et_exit:
    movl $1, %eax
    movl $0, %ebx
    int $0x80
