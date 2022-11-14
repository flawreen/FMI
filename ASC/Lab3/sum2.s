.data
    x: .long 2
    y: .long 3
    s: .space 4
    afisare: .asciz "Suma numerelor %d si %d este %d.\n"
.text
add:
    pushl %ebp
    mov %esp, %ebp

    pushl %ebx

    movl 8(%ebp), %eax
    addl 12(%ebp), %eax

    popl %ebx
    
    popl %ebp
    ret
.globl main
main:
    movl $6, %eax
    movl $5, %ebx

    pushl %eax
    # pushl $s
    pushl y
    pushl x

    call add

    popl %edx
    popl %edx
    popl %edx
    # popl %eax
    movl $s, %ebx
    movl %eax, 0(%ebx)

eticheta:
    # cod suplimentar
    pushl s
    pushl y
    pushl x
    pushl $afisare

    call printf

    popl %edx
    popl %edx
    popl %edx
    popl %edx

    pushl $0
    call fflush
    popl %ebx
    
    mov $1, %eax
    xorl %ebx, %ebx
    int $0x80
    