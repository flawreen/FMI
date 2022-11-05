.data
    x: .long 13  # 1101
    y: .long 10  # 1010
.text

.globl main
main:
    movl x, %eax
a:
    and $1, %eax

    movl x, %eax
b:
    xorl %eax, %eax

    movl x, %eax
d:  
    decl %eax
    movl x, %ebx
    and %eax, %ebx

    movl x, %eax
    movl y, %ebx
e:
    not %ebx
    and %ebx, %eax
    movl %eax, %ecx
    movl y, %ebx
    movl x, %eax
    not %eax
    and %eax, %ebx
    or %ecx, %ebx


etexit:
    movl $1, %eax
    xorl %ebx, %ebx
    int $0x80
