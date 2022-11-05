// var 1
// suma de la 0 la 4 = 10

.data
    n: .long 5

.text

.globl main
main:

    movl $0, %eax # sum = 0
    mov $0, %ecx # i = 0
for:
    cmp n, %ecx
    je et_exit # %ecx < n

    add %ecx, %eax

    incl %ecx
    jmp for

et_exit:
    movl $1, %eax
    movl $0, %ebx
    int $0x80
