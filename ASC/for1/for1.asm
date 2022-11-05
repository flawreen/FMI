.data
    n: .long 5
    s: .space 4

.text
.globl main
main:
    mov $0, %ecx

etloop:
    add %ecx, s
    inc %ecx
    cmp n, %ecx
    je etexit
    jmp etloop
    
etexit:
    movl $1, %eax
    movl $0, %ebx
    int $0x80
