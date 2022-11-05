.data
    formatStr: .asciz "Am citit %d"
    x: .long 5

.text
.globl main
main:
    push x
    push $formatStr
    call printf
    pop %ebx
    pop %edx


