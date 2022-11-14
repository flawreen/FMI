.data
    x: .long 2
    y: .long 3
    s: .space 4
.text
add:
    movl 4(%esp), %eax
    addl 8(%esp), %eax
    movl 12(%esp),%ebx
    movl %eax, 0(%ebx)
    ret
.globl main
main:
    pushl $s
    pushl y
    pushl x
    call add
    popl %edx
    popl %edx
    popl %edx

    mov $1, %eax
    xor %ebx, %ebx
    int $0x80
