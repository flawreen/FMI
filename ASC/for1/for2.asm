.data
    n: .long 5
    s: .space 4

.text
.globl main
main:
    decl n
    movl n, %ecx
    jmp etloop

etloop:
    add %ecx, s
    loop etloop
    jmp etexit

etexit:
    movl $1, %eax
    movl $0, %ebx
    int $0x80
