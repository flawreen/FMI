.data
    x: .long 3
    y: .long 16
    nr: .asciz "Numerele se divid!\n"
.text
.globl main
main:
    mov $0, %edx
    movl x, %eax
    movl y, %ebx
    imul %ebx

    mov $0, %edx
    idiv %ebx

    cmp $0, %edx
    je divid
    jmp exit

divid:
    mov $4, %eax
    mov $1, %ebx
    mov $nr, %ecx
    mov $20, %edx
    int $0x80
    jmp exit

exit:
    mov $1, %eax
    mov $0, %ebx
    int $0x80
