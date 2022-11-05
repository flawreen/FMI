.data
    n: .long 5
    v: .long 10, 20, 30, 40, 50

.text
.globl main
main:
    lea v, %edi
    movl $0, %ecx

etloop:
    cmp n, %ecx
    je etexit

    movl (%edi, %ecx, 4), %edx
    incl %ecx

    jmp etloop

etexit:
    mov $1, %eax
    mov $0, %ebx
    int $0x80

